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


if __name__ == "__main__":
    unittest.main()
