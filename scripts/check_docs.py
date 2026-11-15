"""Check this repository's deliberately small Markdown subset, offline."""

import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


IMPORTS = {
    "docs/manifesto.md": ("deep-research-report (2).md", "baseline"),
    "docs/historical/deep-research-draft.md": (
        "deep-research-report (1).md", "historical-draft"
    ),
}
REQUIRED = (
    "README.md", "CONTRIBUTING.md", "CHANGELOG.md", "LICENSE",
    "LICENSES/CC-BY-4.0.txt", "LICENSES/MIT.txt", "docs/imports.json",
    "docs/import-notes.md", "docs/project-manifesto.md", "docs/research-method.md", "docs/roadmap.md",
    "docs/stage-review-2026-11.md", "docs/glossary.md", "docs/engineering-practice-guide.md",
    "docs/obsidian.md", "research/sources.md", *IMPORTS,
    "docs/knowledge-architecture.md", "docs/decisions.md",
    "knowledge/README.md", "knowledge/vocabulary.json", "knowledge/claims.json",
    "scripts/check_docs.py", "tests/test_check_docs.py",
    ".github/workflows/docs.yml", ".gitignore", ".gitattributes",
)
NAVIGATION = (
    "docs/project-manifesto.md", "docs/manifesto.md", "docs/import-notes.md", "docs/research-method.md",
    "research/sources.md", "docs/roadmap.md", "docs/obsidian.md",
    "docs/stage-review-2026-11.md", "docs/glossary.md", "docs/engineering-practice-guide.md",
    "docs/knowledge-architecture.md", "docs/decisions.md", "knowledge/README.md",
    "CONTRIBUTING.md", "CHANGELOG.md", "LICENSE",
)
LINK = re.compile(r"!?\[[^\[\]\n]*\]\(([^\s()<>]+)\)")
ANCHOR = re.compile(r'<a id="([A-Za-z][A-Za-z0-9_-]*)"></a>')
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def prose(text):
    """Remove fenced/inline examples; return prose and fence diagnostics."""
    lines, errors = [], []
    marker, language, content = "", "", []
    for line in text.splitlines():
        match = FENCE.match(line)
        if marker:
            if (match and match[1][0] == marker[0]
                    and len(match[1]) >= len(marker) and not match[2].strip()):
                if language == "mermaid" and not "\n".join(content).strip():
                    errors.append("empty Mermaid block")
                marker, language, content = "", "", []
            else:
                content.append(line)
        elif match:
            marker, language = match[1], match[2].strip()
        else:
            lines.append(line)
    if marker:
        errors.append("unclosed fence")
    visible = "\n".join(lines)
    visible = re.sub(r"(`+).*?\1", "", visible)
    return visible, errors


def check_imports(root):
    errors, preserved = [], set()
    try:
        records = json.loads((root / "docs/imports.json").read_text(encoding="utf-8"))["records"]
        if (not isinstance(records, list) or len(records) != 2
                or {r["path"] for r in records} != set(IMPORTS)):
            return ["import registry must contain exactly the two approved paths"], preserved
        for record in records:
            name = record["path"]
            source, role = IMPORTS[name]
            if (record["source_filename"] != source or record["role"] != role
                    or set(record["exceptions"]) != {"export-citations", "original-format"}
                    or not isinstance(record["reason"], str) or not record["reason"].strip()
                    or not re.fullmatch(r"[0-9a-f]{64}", record["sha256"])):
                errors.append(f"{name}: invalid import metadata")
                continue
            path = root / name
            if not path.resolve().is_relative_to(root.resolve()):
                errors.append(f"{name}: outside repository")
                continue
            body = path.read_bytes()
            if len(body) != record["bytes"] or hashlib.sha256(body).hexdigest() != record["sha256"]:
                errors.append(f"{name}: integrity mismatch")
            else:
                preserved.add(name)
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors.append(f"invalid import registry: {error}")
    return errors, preserved


def check_target(root, source, url):
    parts = urlsplit(url)
    if parts.scheme in {"https", "http", "mailto"}:
        return []
    if parts.scheme or parts.netloc or parts.query or "\\" in url or parts.path.startswith("/"):
        return [f"unsupported link: {url}"]
    decoded = unquote(parts.path)
    if "\\" in decoded or ":" in decoded or decoded.startswith("/"):
        return [f"unsupported link: {url}"]
    target = source.parent / decoded if decoded else source
    resolved = target.resolve()
    if not resolved.is_relative_to(root.resolve()):
        return [f"outside repository: {url}"]
    # Inspect spelling using directory entries, including on case-insensitive Windows.
    relative = Path(os.path.normpath(target)).relative_to(root)
    current = root
    for part in relative.parts:
        if not current.is_dir() or part not in {p.name for p in current.iterdir()}:
            return [f"missing target (case or missing path component): {url}"]
        current /= part
    if not current.is_file():
        return [f"missing target file: {url}; link to a file, not a directory"]
    if parts.fragment:
        try:
            visible, _ = prose(current.read_text(encoding="utf-8"))
        except (OSError, UnicodeError):
            return [f"anchor target is not UTF-8 text: {url}"]
        if unquote(parts.fragment) not in ANCHOR.findall(visible):
            return [f"missing explicit anchor: {url}"]
    return []


def check_markdown(root, path, preserved=False):
    label = path.relative_to(root).as_posix()
    try:
        text = path.read_bytes().decode("utf-8")
    except (OSError, UnicodeError) as error:
        return [f"{label}: invalid UTF-8 document: {error}"]
    visible, errors = prose(text)
    if not preserved:
        if "\r" in text:
            errors.append("use LF line endings")
        if not text.endswith("\n"):
            errors.append("missing final newline")
        if len(re.findall(r"^# \S", visible, flags=re.MULTILINE)) != 1:
            errors.append("expected exactly one H1")
        if "" in text or "" in text or "" in text:
            errors.append("unresolved export citation")
        anchors = ANCHOR.findall(visible)
        if len(anchors) != len(set(anchors)):
            errors.append("duplicate anchor")
        remainder = LINK.sub("", visible)
        if (re.search(r"\[[^\]\n]+\](?:\(|\[|:)", remainder)
                or "[[" in remainder or re.search(r"<\s*(?:a\b[^>]*href|img\b)", remainder, re.I)):
            errors.append("unsupported link syntax; use simple inline Markdown links")
    for match in LINK.finditer(visible):
        try:
            errors.extend(check_target(root, path, match[1]))
        except (ValueError, OSError) as error:
            errors.append(f"invalid link {match[1]}: {error}")
    return [f"{label}: {error}" for error in errors]


def check_repository(root):
    root = root.resolve()
    errors = [f"required file missing: {name}" for name in REQUIRED if not (root / name).is_file()]
    import_errors, preserved = check_imports(root)
    errors.extend(import_errors)
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if any(part in {".git", ".venv", "__pycache__"} for part in relative.parts):
            continue
        if not path.resolve().is_relative_to(root):
            errors.append(f"outside repository: {relative.as_posix()}")
            continue
        errors.extend(check_markdown(root, path, relative.as_posix() in preserved))
    readme = root / "README.md"
    if readme.is_file():
        try:
            visible, _ = prose(readme.read_text(encoding="utf-8"))
            targets = {match[1] for match in LINK.finditer(visible)}
            errors.extend(f"README navigation missing: {name}" for name in NAVIGATION if name not in targets)
        except UnicodeError:
            pass  # check_markdown already reports invalid UTF-8.
    return errors


# --- Knowledge layer: topic metadata, claim register and generated map ---

TOPIC_FIELDS = ("id", "title", "question", "entry", "maturity", "status", "domains", "axes",
                "readers", "related", "edit_source", "provenance", "first_public", "last_revised")
STATUS_FIELDS = ("editorial", "human_review", "evidence", "experiment")
CLAIM_FIELDS = ("id", "statement", "type", "status", "axes", "topics", "evidence", "practice",
                "falsified_by", "history")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
CLAIM_ID = re.compile(r"K-\d{3}")
RULE = re.compile(r"\*\*(G-\d+)（")
INDEX = "knowledge/README.md"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def topic_dirs(root):
    base = root / "research"
    return sorted(p for p in base.iterdir() if p.is_dir()) if base.is_dir() else []


def load_knowledge(root):
    """Return (vocabulary, topics by id, claims, errors)."""
    errors, topics, claims = [], {}, []
    try:
        vocab = load_json(root / "knowledge/vocabulary.json")
    except (OSError, ValueError) as error:
        return {}, {}, [], [f"knowledge/vocabulary.json: {error}"]
    for folder in topic_dirs(root):
        label = folder.relative_to(root).as_posix() + "/meta.json"
        try:
            meta = load_json(folder / "meta.json")
        except (OSError, ValueError) as error:
            errors.append(f"{label}: missing or invalid topic metadata: {error}")
            continue
        topics[folder.name] = meta
        if tuple(meta) != TOPIC_FIELDS:
            errors.append(f"{label}: fields must be exactly, in order: {', '.join(TOPIC_FIELDS)}")
            continue
        if meta["id"] != folder.name:
            errors.append(f"{label}: id must equal folder name")
        if not (folder / "README.md").is_file():
            errors.append(f"{label}: topic README.md missing")
        if not (folder / meta["entry"]).is_file():
            errors.append(f"{label}: entry not found: {meta['entry']}")
        if meta["provenance"] is not None and not (folder / meta["provenance"]).is_file():
            errors.append(f"{label}: provenance not found: {meta['provenance']}")
        if meta["maturity"] not in vocab["maturity"]:
            errors.append(f"{label}: unknown maturity {meta['maturity']}")
        if meta["edit_source"] not in vocab["edit_source"]:
            errors.append(f"{label}: unknown edit_source {meta['edit_source']}")
        status = meta["status"]
        if not isinstance(status, dict) or tuple(status) != STATUS_FIELDS:
            errors.append(f"{label}: status fields must be {', '.join(STATUS_FIELDS)}")
        else:
            errors.extend(f"{label}: unknown {k} {v}" for k, v in status.items() if v not in vocab[k])
        for key, table in (("domains", "domains"), ("axes", "axes"), ("readers", "readers")):
            if not meta[key] or len(set(meta[key])) != len(meta[key]):
                errors.append(f"{label}: {key} must be a non-empty list without duplicates")
            errors.extend(f"{label}: unknown {key[:-1]} {v}" for v in meta[key] if v not in vocab[table])
        for key in ("first_public", "last_revised"):
            if not DATE.fullmatch(str(meta[key])):
                errors.append(f"{label}: {key} must be YYYY-MM-DD")
        if meta["maturity"] in {"reviewed", "tested", "stable"} and status.get("human_review") != "passed":
            errors.append(f"{label}: maturity {meta['maturity']} requires human_review passed")
        if meta["maturity"] in {"tested", "stable"} and status.get("experiment") == "not-run":
            errors.append(f"{label}: maturity {meta['maturity']} requires an executed experiment")
    for slug, meta in topics.items():
        for other in meta.get("related", []):
            if other not in topics or other == slug:
                errors.append(f"research/{slug}/meta.json: unknown related topic {other}")
    try:
        claims = load_json(root / "knowledge/claims.json")["claims"]
    except (OSError, ValueError, KeyError) as error:
        return vocab, topics, [], errors + [f"knowledge/claims.json: {error}"]
    guide = root / "docs/engineering-practice-guide.md"
    rules = set(RULE.findall(guide.read_text(encoding="utf-8"))) if guide.is_file() else set()
    seen = set()
    for claim in claims:
        label = f"knowledge/claims.json: {claim.get('id', '?')}"
        if tuple(k for k in claim if k != "note") != CLAIM_FIELDS:
            errors.append(f"{label}: fields must be {', '.join(CLAIM_FIELDS)} (+ optional note)")
            continue
        if not CLAIM_ID.fullmatch(claim["id"]) or claim["id"] in seen:
            errors.append(f"{label}: id must be unique K-NNN")
        seen.add(claim["id"])
        for key, table in (("type", "claim_type"), ("status", "claim_status")):
            if claim[key] not in vocab[table]:
                errors.append(f"{label}: unknown {key} {claim[key]}")
        if not claim["axes"]:
            errors.append(f"{label}: at least one axis required")
        errors.extend(f"{label}: unknown axis {a}" for a in claim["axes"] if a not in vocab["axes"])
        errors.extend(f"{label}: unknown topic {t}" for t in claim["topics"] if t not in topics)
        if not claim["evidence"]:
            errors.append(f"{label}: at least one evidence entry required")
        for item in claim["evidence"]:
            target = root / item["path"]
            if not target.resolve().is_relative_to(root.resolve()) or not target.is_file():
                errors.append(f"{label}: evidence path not found: {item['path']}")
        errors.extend(f"{label}: unknown practice rule {r}" for r in claim["practice"] if r not in rules)
        if claim["type"] == "hypothesis" and claim["status"] == "supported":
            errors.append(f"{label}: a hypothesis cannot be supported without changing its type")
        if not claim["history"] or any(not DATE.fullmatch(h.get("date", "")) for h in claim["history"]):
            errors.append(f"{label}: history needs dated entries")
    return vocab, topics, claims, errors


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def render_index(root):
    vocab, topics, claims, errors = load_knowledge(root)
    if errors:
        return None
    link = lambda slug: f"[{topics[slug]['title']}](../research/{slug}/README.md)"
    status = lambda s: "／".join(vocab[k][v].split("：")[0] for k, v in s.items())
    out = [
        "# 知识地图", "",
        "本页由 `python -I scripts/check_docs.py --write-index` 根据各专题的 `meta.json`、"
        "[命题登记](claims.json)与[受控词表](vocabulary.json)生成，请勿手工编辑；检查器会拒绝过期版本。"
        "架构与维护规则见[知识库架构](../docs/knowledge-architecture.md)。", "",
        "## 专题", "",
        "| 专题 | 核心问题 | 成熟度 | 编辑／审核／证据／实验 |",
        "|---|---|---|---|",
    ]
    for slug in sorted(topics):
        t = topics[slug]
        out.append(f"| {link(slug)} | {cell(t['question'])} | {vocab['maturity'][t['maturity']].split('：')[0]} "
                   f"| {status(t['status'])} |")
    out += ["", "## 按领域", "", "| 领域 | 专题 |", "|---|---|"]
    for key, name in vocab["domains"].items():
        hits = [link(s) for s in sorted(topics) if key in topics[s]["domains"]]
        if hits:
            out.append(f"| {name} | {'、'.join(hits)} |")
    out += ["", "## 按读者", "", "| 读者 | 专题 |", "|---|---|"]
    for key, name in vocab["readers"].items():
        hits = [link(s) for s in sorted(topics) if key in topics[s]["readers"]]
        if hits:
            out.append(f"| {name} | {'、'.join(hits)} |")
    out += ["", "## 命题：按责任—证据—限度", "",
            "一条命题可以落在多条轴上，此处按第一条轴归类。类型与状态的含义见受控词表；"
            "“有支撑”只在所列证据范围内成立，不等于经过人工审核或实验。"]
    for axis, name in vocab["axes"].items():
        rows = [c for c in claims if c["axes"][0] == axis]
        if not rows:
            continue
        out += ["", f"### {name.split('：')[0]}", "", "| 编号 | 命题 | 类型 | 状态 | 专题 | 实践规则 |", "|---|---|---|---|---|---|"]
        for c in rows:
            ts = "、".join(link(t) for t in c["topics"]) or "（宗旨）"
            rules = "、".join(c["practice"]) or "—"
            out.append(f"| {c['id']} | {cell(c['statement'])} | {vocab['claim_type'][c['type']]} "
                       f"| {vocab['claim_status'][c['status']].split('：')[0]} | {ts} | {rules} |")
    open_items = [c for c in claims if c["status"] in {"contested", "proposed"} or c["type"] == "hypothesis"]
    out += ["", "## 待处理：受质疑、仅提出或待验证的命题", "", "| 编号 | 状态 | 推翻条件或缺口 |", "|---|---|---|"]
    for c in open_items:
        gap = c.get("note") or c["falsified_by"] or "—"
        out.append(f"| {c['id']} | {vocab['claim_status'][c['status']].split('：')[0]} | {cell(gap)} |")
    out += ["", "## 命题证据", "", "| 编号 | 证据位置 |", "|---|---|"]
    for c in claims:
        refs = "；".join(f"[{cell(e['note'])}](../{e['path']})" for e in c["evidence"])
        out.append(f"| {c['id']} | {refs} |")
    out += ["", "返回[项目首页](../README.md)。", ""]
    return "\n".join(out)


def check_knowledge(root):
    root = root.resolve()
    _, _, _, errors = load_knowledge(root)
    if errors:
        return errors
    index = root / INDEX
    expected = render_index(root)
    if not index.is_file() or index.read_text(encoding="utf-8") != expected:
        return [f"{INDEX}: out of date; run python -I scripts/check_docs.py --write-index"]
    return []


def main():
    root = Path(__file__).resolve().parents[1]
    if "--write-index" in sys.argv[1:]:
        _, _, _, problems = load_knowledge(root)
        for problem in problems:
            print(f"FAIL: {problem}")
        if problems:
            return 1
        (root / INDEX).write_text(render_index(root), encoding="utf-8", newline="\n")
        print(f"WROTE: {INDEX}")
        return 0
    errors = check_knowledge(root) + check_repository(root)
    for error in errors:
        print(f"FAIL: {error}")
    if errors:
        print(f"FAILED: {len(errors)} document check(s)")
        return 1
    print("PASS: required files, scoped Markdown format, local links and README navigation")
    print("PASS: topic metadata, claim register and generated knowledge map are consistent")
    print("PASS: both registered imports match their recorded SHA-256 and byte counts")
    print("EXCEPTIONS: only the two exact imports retain original formatting/export citations")
    print("NOT VERIFIED: external evidence, external URLs, Mermaid syntax/rendering, Obsidian UI, Unity behavior")
    return 0


if __name__ == "__main__":
    sys.exit(main())
