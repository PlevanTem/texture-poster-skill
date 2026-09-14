#!/usr/bin/env python3
"""Validate the distributable Texture Poster skill package without third-party modules."""

from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path


REQUIRED = (
    "SKILL.md",
    "README.md",
    "artifact-template.json",
    "agents/openai.yaml",
    "assets/reference.png",
    "assets/preview.png",
    "references/creative-brief.md",
    "references/art-direction.md",
    "references/generation-workflow.md",
    "references/source-and-rights.md",
    "references/quality-gates.md",
    "references/case-studies.md",
    "examples/brand-source-studies/case-index.json",
    "examples/brand-source-studies/source-to-poster-contact-sheet.png",
)


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as stream:
        header = stream.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">II", header[16:24])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path)
    args = parser.parse_args()
    root = (args.root or Path(__file__).resolve().parents[1]).resolve()
    errors: list[str] = []

    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing: {rel}")

    if errors:
        print("FAIL")
        print("\n".join(errors))
        return 1

    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    frontmatter_match = re.match(r"^---\n(.*?)\n---", skill, re.DOTALL)
    if not frontmatter_match:
        errors.append("SKILL.md frontmatter is missing or malformed")
    else:
        frontmatter = frontmatter_match.group(1)
        keys = set(re.findall(r"^([A-Za-z0-9_-]+):", frontmatter, re.MULTILINE))
        unexpected = keys - {"name", "description", "license", "allowed-tools", "metadata"}
        if unexpected:
            errors.append(f"unexpected SKILL.md frontmatter keys: {', '.join(sorted(unexpected))}")
        name_match = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.MULTILINE)
        name = name_match.group(1).strip().strip('"\'') if name_match else ""
        if name != "texture-poster-skill" or not re.fullmatch(r"[a-z0-9-]{1,64}", name):
            errors.append("SKILL.md frontmatter has an invalid name")
        description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
        description = description_match.group(1).strip().strip('"\'') if description_match else ""
        if not description or len(description) > 1024 or "<" in description or ">" in description:
            errors.append("SKILL.md frontmatter has an invalid description")
    if re.search(r"^\s*\[TODO:[^\n]*\]\s*$", skill, re.MULTILINE):
        errors.append("SKILL.md contains an unfinished TODO placeholder")

    artifact = json.loads((root / "artifact-template.json").read_text(encoding="utf-8"))
    for key in ("reference", "preview"):
        rel = artifact.get(key)
        if not isinstance(rel, str) or not (root / rel).is_file():
            errors.append(f"artifact-template.json {key} path is invalid")

    index_path = root / "examples/brand-source-studies/case-index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    cases = index.get("cases", [])
    if len(cases) != 5:
        errors.append(f"expected 5 showcase cases, found {len(cases)}")
    required_case_fields = {
        "id", "brand", "sector", "source_page", "source_asset_url", "poster",
        "concept", "retained_facts", "removed_context", "generated_additions",
        "source_role", "rights_status", "sha256",
    }
    for case in cases:
        missing = sorted(required_case_fields - set(case))
        if missing:
            errors.append(f"{case.get('id', 'unknown')} missing fields: {', '.join(missing)}")
            continue
        poster = index_path.parent / case["poster"]
        if not poster.is_file():
            errors.append(f"missing poster: {poster.relative_to(root)}")
        else:
            try:
                if png_size(poster) != (1122, 1402):
                    errors.append(f"unexpected poster size: {poster.name} {png_size(poster)}")
            except ValueError as exc:
                errors.append(f"{poster.name}: {exc}")

    sheet = index_path.parent / index.get("contact_sheet", "")
    if not sheet.is_file() or png_size(sheet) != (2200, 3100):
        errors.append("contact sheet is missing or is not 2200x3100")

    readme = (root / "README.md").read_text(encoding="utf-8")
    for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", readme):
        if not target.startswith(("http://", "https://")) and not (root / target).is_file():
            errors.append(f"README image target missing: {target}")

    if errors:
        print("FAIL")
        print("\n".join(errors))
        return 1

    print(f"PASS: {root}")
    print(f"showcase_cases={len(cases)}")
    print("poster_size=1122x1402")
    print("contact_sheet_size=2200x3100")
    return 0


if __name__ == "__main__":
    sys.exit(main())
