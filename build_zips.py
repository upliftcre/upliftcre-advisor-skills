#!/usr/bin/env python3
"""Build one upload-ready zip per skill into dist/.

Each zip holds a single top-level folder named after the skill, with SKILL.md
directly inside it. That is the layout Claude's skill upload expects.

Run from anywhere:  python build_zips.py
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
SKILLS = ["upliftcre-blog-article", "upliftcre-market-report", "upliftcre-listing", "upliftcre-case-study"]
FIXED_TIME = (2026, 10, 22, 0, 0, 0)  # stable timestamps, so a rebuild with no change gives the same zip


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        raise SystemExit("no frontmatter")
    out = {}
    for line in m.group(1).splitlines():
        key, _, val = line.partition(":")
        out[key.strip()] = val.strip()
    return out


def check(skill):
    folder = ROOT / skill
    text = (folder / "SKILL.md").read_text(encoding="utf-8")
    if "\r" in text:
        raise SystemExit(f"{skill}: SKILL.md has CRLF line endings")
    fm = frontmatter(text)
    if set(fm) != {"name", "description"}:
        raise SystemExit(f"{skill}: frontmatter keys must be name + description, got {sorted(fm)}")
    if fm["name"] != skill:
        raise SystemExit(f"{skill}: name '{fm['name']}' does not match folder")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", fm["name"]) or len(fm["name"]) > 64:
        raise SystemExit(f"{skill}: bad name")
    d = fm["description"]
    if not d or len(d) > 1024 or "<" in d or ">" in d:
        raise SystemExit(f"{skill}: description empty, over 1024 chars, or has angle brackets ({len(d)})")
    if len(list(folder.rglob("SKILL.md"))) != 1:
        raise SystemExit(f"{skill}: must contain exactly one SKILL.md")
    for ref in re.findall(r"`(references/[^`]+)`", text):
        if not (folder / ref).is_file():
            raise SystemExit(f"{skill}: SKILL.md points to missing file {ref}")
    return len(text.splitlines()), len(d)


def build(skill):
    lines, dlen = check(skill)
    folder = ROOT / skill
    DIST.mkdir(exist_ok=True)
    target = DIST / f"{skill}.zip"
    files = sorted(p for p in folder.rglob("*") if p.is_file())
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            arc = f"{skill}/{p.relative_to(folder).as_posix()}"
            info = zipfile.ZipInfo(arc, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes())
    with zipfile.ZipFile(target) as z:
        names = z.namelist()
    tops = {n.split("/")[0] for n in names}
    if tops != {skill} or f"{skill}/SKILL.md" not in names:
        raise SystemExit(f"{skill}: zip layout wrong: {names}")
    print(f"{target.name}: {len(names)} files, SKILL.md {lines} lines, description {dlen} chars")
    for n in names:
        print(f"   {n}")


if __name__ == "__main__":
    for s in SKILLS:
        build(s)
    sys.exit(0)
