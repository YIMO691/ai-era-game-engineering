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
    "docs/import-notes.md", "docs/research-method.md", "docs/roadmap.md",
    "docs/obsidian.md", "research/sources.md", *IMPORTS,
    "scripts/check_docs.py", "tests/test_check_docs.py",
    ".github/workflows/docs.yml", ".gitignore", ".gitattributes",
)
NAVIGATION = (
    "docs/manifesto.md", "docs/import-notes.md", "docs/research-method.md",
    "research/sources.md", "docs/roadmap.md", "docs/obsidian.md",
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


def main():
    root = Path(__file__).resolve().parents[1]
    errors = check_repository(root)
    for error in errors:
        print(f"FAIL: {error}")
    if errors:
        print(f"FAILED: {len(errors)} document check(s)")
        return 1
    print("PASS: required files, scoped Markdown format, local links and README navigation")
    print("PASS: both registered imports match their recorded SHA-256 and byte counts")
    print("EXCEPTIONS: only the two exact imports retain original formatting/export citations")
    print("NOT VERIFIED: external evidence, external URLs, Mermaid syntax/rendering, Obsidian UI, Unity behavior")
    return 0


if __name__ == "__main__":
    sys.exit(main())
