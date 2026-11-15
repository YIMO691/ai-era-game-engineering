import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_docs.py"
checker = None
if SCRIPT.exists():
    spec = importlib.util.spec_from_file_location("check_docs", SCRIPT)
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)


class DocumentChecks(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(checker, "Document checker has not been implemented")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        return path

    def check(self, text, name="README.md"):
        return checker.check_markdown(self.root, self.write(name, text))

    def assert_error(self, errors, phrase):
        self.assertTrue(any(phrase in error for error in errors), errors)

    def test_valid_relative_link(self):
        self.write("docs/方法.md", "# 方法\n")
        self.assertEqual([], self.check("# Home\n\n[Method](docs/%E6%96%B9%E6%B3%95.md)\n"))

    def test_missing_link(self):
        self.assert_error(self.check("# Home\n\n[Missing](missing.md)\n"), "missing target")

    def test_wrong_case(self):
        self.write("docs/Method.md", "# Method\n")
        self.assert_error(self.check("# Home\n\n[Method](docs/method.md)\n"), "case or missing")

    def test_escape_repository(self):
        self.assert_error(self.check("# Home\n\n[Outside](../outside.md)\n"), "outside repository")

    def test_absolute_local_path(self):
        self.assert_error(self.check("# Home\n\n[Private](file:///private.md)\n"), "unsupported link")

    def test_external_links_not_fetched(self):
        self.assertEqual([], self.check("# Home\n\n[Example](https://example.invalid/a)\n"))

    def test_valid_explicit_anchor(self):
        self.write("docs/method.md", '# Method\n\n<a id="scope"></a>\n')
        self.assertEqual([], self.check("# Home\n\n[Scope](docs/method.md#scope)\n"))

    def test_missing_anchor(self):
        self.write("docs/method.md", "# Method\n")
        self.assert_error(self.check("# Home\n\n[Scope](docs/method.md#scope)\n"), "missing explicit anchor")

    def test_duplicate_anchor(self):
        self.assert_error(self.check('# Home\n<a id="scope"></a>\n<a id="scope"></a>\n'), "duplicate anchor")

    def test_fenced_and_inline_code_links_ignored(self):
        text = '# Home\n\n`[example](missing.md)`\n\n```md\n[example](missing.md)\n```\n'
        self.assertEqual([], self.check(text))

    def test_new_export_citation_rejected_even_in_fence(self):
        self.assert_error(self.check("# Home\n\n```text\nciteunresolved\n```\n"), "export citation")

    def test_unclosed_fence(self):
        self.assert_error(self.check("# Home\n\n```python\npass\n"), "unclosed fence")

    def test_empty_mermaid(self):
        self.assert_error(self.check("# Home\n\n```mermaid\n\n```\n"), "empty Mermaid")

    def test_multiple_h1(self):
        self.assert_error(self.check("# One\n\n# Two\n"), "one H1")

    def test_missing_final_newline(self):
        self.assert_error(self.check("# Home"), "final newline")

    def test_reference_style_rejected(self):
        self.assert_error(self.check("# Home\n\n[Method][m]\n\n[m]: method.md\n"), "unsupported link syntax")

    def test_complex_inline_link_rejected(self):
        self.assert_error(self.check('# Home\n\n[Method](method.md "Title")\n'), "unsupported link syntax")

    def test_wikilink_rejected_in_public_docs(self):
        self.assert_error(self.check("# Home\n\n[[Private]]\n"), "unsupported link syntax")

    def make_imports(self):
        records = []
        for path, source, role in (
            ("docs/manifesto.md", "deep-research-report (2).md", "baseline"),
            ("docs/historical/deep-research-draft.md", "deep-research-report (1).md", "historical-draft"),
        ):
            file = self.write(path, "# Original\n\nciteunresolved")
            body = file.read_bytes()
            records.append({"path": path, "source_filename": source, "role": role,
                            "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body),
                            "exceptions": ["export-citations", "original-format"],
                            "reason": "Preserve supplied original, not verified evidence."})
        self.write("docs/imports.json", json.dumps({"records": records}))
        return records

    def test_registered_imports_keep_exact_bytes(self):
        self.make_imports()
        errors, preserved = checker.check_imports(self.root)
        self.assertEqual([], errors)
        self.assertEqual(2, len(preserved))
        for name in preserved:
            self.assertEqual([], checker.check_markdown(self.root, self.root / name, preserved=True))

    def test_changed_import_not_exempt(self):
        self.make_imports()
        self.write("docs/manifesto.md", "# Changed\n")
        errors, preserved = checker.check_imports(self.root)
        self.assert_error(errors, "integrity mismatch")
        self.assertNotIn("docs/manifesto.md", preserved)

    def test_arbitrary_import_exception_rejected(self):
        records = self.make_imports()
        records[0]["path"] = "README.md"
        self.write("docs/imports.json", json.dumps({"records": records}))
        errors, _ = checker.check_imports(self.root)
        self.assert_error(errors, "exactly the two approved")

    def test_invalid_import_json_reported(self):
        self.write("docs/imports.json", "{")
        errors, preserved = checker.check_imports(self.root)
        self.assert_error(errors, "invalid import registry")
        self.assertEqual(set(), preserved)

    def test_required_files_missing(self):
        errors = checker.check_repository(self.root)
        self.assert_error(errors, "required file missing")

    def test_project_manifesto_is_required(self):
        self.assertIn("docs/project-manifesto.md", checker.REQUIRED)

    def test_readme_requires_both_manifesto_and_report(self):
        self.assertIn("docs/project-manifesto.md", checker.NAVIGATION)
        self.assertIn("docs/manifesto.md", checker.NAVIGATION)

    def test_stage_review_and_glossary_are_required_and_linked(self):
        for name in ("docs/stage-review-2026-11.md", "docs/glossary.md",
                     "docs/engineering-practice-guide.md"):
            self.assertIn(name, checker.REQUIRED)
            self.assertIn(name, checker.NAVIGATION)


REPO = Path(__file__).resolve().parents[1]


class KnowledgeChecks(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(checker, "Document checker has not been implemented")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        vocab = (REPO / "knowledge/vocabulary.json").read_text(encoding="utf-8")
        self.write("knowledge/vocabulary.json", vocab)
        self.write("docs/engineering-practice-guide.md", "# Guide\n\n**G-1（必须）** rule\n")
        self.write("research/alpha/README.md", "# Alpha\n")
        self.write("research/alpha/report.md", "# Report\n")
        self.meta = {
            "id": "alpha", "title": "甲", "question": "问题？", "entry": "report.md",
            "maturity": "drafted",
            "status": {"editorial": "draft", "human_review": "pending",
                       "evidence": "partial", "experiment": "not-run"},
            "domains": ["async-lifecycle"], "axes": ["ownership"], "readers": ["practitioner"],
            "related": [], "edit_source": "public", "provenance": None,
            "first_public": "2026-11-15", "last_revised": "2026-11-15",
        }
        self.claim = {
            "id": "K-001", "statement": "命题", "type": "inference", "status": "supported",
            "axes": ["ownership"], "topics": ["alpha"],
            "evidence": [{"path": "research/alpha/report.md", "note": "第1节"}],
            "practice": ["G-1"], "falsified_by": None,
            "history": [{"date": "2026-11-15", "change": "登记", "reason": "测试"}],
        }
        self.save()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        return path

    def save(self):
        self.write("research/alpha/meta.json", json.dumps(self.meta, ensure_ascii=False))
        self.write("knowledge/claims.json", json.dumps({"claims": [self.claim]}, ensure_ascii=False))

    def errors(self):
        return checker.load_knowledge(self.root)[3]

    def assert_error(self, phrase):
        errors = self.errors()
        self.assertTrue(any(phrase in error for error in errors), errors)

    def test_valid_knowledge_and_fresh_index(self):
        self.assertEqual([], self.errors())
        self.assert_index_state(fresh=False)  # no index written yet
        self.write("knowledge/README.md", checker.render_index(self.root))
        self.assertEqual([], checker.check_knowledge(self.root))

    def assert_index_state(self, fresh):
        errors = checker.check_knowledge(self.root)
        self.assertEqual(fresh, not errors, errors)

    def test_stale_index_is_rejected(self):
        self.write("knowledge/README.md", checker.render_index(self.root))
        self.claim["statement"] = "改过的命题"
        self.save()
        self.assertTrue(any("out of date" in e for e in checker.check_knowledge(self.root)))

    def test_topic_without_meta_is_rejected(self):
        self.write("research/beta/README.md", "# Beta\n")
        self.assert_error("missing or invalid topic metadata")

    def test_unknown_vocabulary_value(self):
        self.meta["domains"] = ["blockchain"]
        self.save()
        self.assert_error("unknown domain blockchain")

    def test_reviewed_requires_passed_review(self):
        self.meta["maturity"] = "reviewed"
        self.save()
        self.assert_error("requires human_review passed")

    def test_tested_requires_experiment(self):
        self.meta["maturity"] = "tested"
        self.meta["status"]["human_review"] = "passed"
        self.save()
        self.assert_error("requires an executed experiment")

    def test_missing_entry_and_related(self):
        self.meta["entry"] = "missing.md"
        self.meta["related"] = ["ghost"]
        self.save()
        self.assert_error("entry not found")
        self.assert_error("unknown related topic ghost")

    def test_hypothesis_cannot_be_supported(self):
        self.claim["type"] = "hypothesis"
        self.save()
        self.assert_error("hypothesis cannot be supported")

    def test_claim_references_must_exist(self):
        self.claim["evidence"] = [{"path": "research/alpha/nope.md", "note": "x"}]
        self.claim["practice"] = ["G-99"]
        self.claim["topics"] = ["ghost"]
        self.save()
        self.assert_error("evidence path not found")
        self.assert_error("unknown practice rule G-99")
        self.assert_error("unknown topic ghost")

    def test_duplicate_claim_ids(self):
        self.write("knowledge/claims.json", json.dumps({"claims": [self.claim, dict(self.claim)]}))
        self.assert_error("id must be unique")

    def test_repository_knowledge_layer_is_registered(self):
        for name in ("docs/knowledge-architecture.md", "docs/decisions.md", "knowledge/README.md"):
            self.assertIn(name, checker.REQUIRED)
            self.assertIn(name, checker.NAVIGATION)
        self.assertEqual([], checker.check_knowledge(REPO))


if __name__ == "__main__":
    unittest.main()
