<div align="center">

# Texture Poster

**A texture-driven editorial poster skill**

Transform an ordinary photograph, product image, or brand theme into an editorial poster where real material texture carries the concept.

[简体中文](README.md) · [English](README.en.md)

![Agent Skill](https://img.shields.io/badge/Agent-Skill-111111?style=flat-square)
![Codex Compatible](https://img.shields.io/badge/Codex-Compatible-111111?style=flat-square&logo=openai&logoColor=white)
![Output Editorial Poster](https://img.shields.io/badge/Output-Editorial_Poster-6B5B4B?style=flat-square)
![Brand Studies 5](https://img.shields.io/badge/Brand_Studies-5-8A6F4D?style=flat-square)
![Validator Python stdlib](https://img.shields.io/badge/Validator-Python_stdlib-3776AB?style=flat-square&logo=python&logoColor=white)

</div>

This is not a tool for placing a texture overlay on a photograph. It removes irrelevant context first, then uses material texture, scale, light, negative space, and precise typography to communicate an indirect association.

![Five brand source-to-texture-poster studies](examples/brand-source-studies/source-to-poster-contact-sheet.png)

## Start in 30 seconds

In an agent that supports Skills, local image access, and image generation or editing, say:

```text
Use $texture-poster-skill to transform this product image into a 4:5 texture-driven poster.
Do not preserve the complete product. Keep only 2–3 irreplaceable material facts; create a text-free master first, then typeset the final copy precisely.
```

You can also begin with a theme alone:

```text
Use $texture-poster-skill to create a poster about “a boundary becoming permeable.”
Choose the primary material yourself. Use one transformation relationship, do not display a grid, and do not make a nine-panel collage.
```

## What it does

- Separates the input into material facts, identity anchors, and removable context instead of preserving the full photograph by default.
- Selects material through one “physical property → conceptual perception” proposition, keeping texture from becoming decoration.
- Establishes one focal point through macro scale, scale shifts, redistributed area, contact boundaries, or phase transitions.
- Generates a text-free visual master first; accurate typography is added only after the master passes hard gates.
- Uses an invisible grid to organize alignment, whitespace, and reading order without drawing guide lines into the final image.
- Records source, access date, intended use, model-added content, and rights status for web-sourced assets.
- Uses five hard gates and a 100-point rubric to distinguish finished work, direction studies, and failed drafts.

## How it works

```text
Input: image or text
      ↓
Interpret: concept verb + physical material properties
      ↓
Subtract: retain 2–3 facts / remove 50%–70% of the scene
      ↓
Focus: one focal point + one experimental action + invisible grid
      ↓
Design: text-free visual master → five hard gates
      ↓
Typeset: precise real-font typography → thumbnail and source checks
      ↓
Validate: score ≥80 with no hard failure → deliver
```

See [SKILL.md](SKILL.md) for the complete execution instructions.

## Five brand studies

All works below are unofficial experiments testing whether the same design mechanism can work across five categories. They are not brand commissions and do not imply commercial publication rights.

| Outdoor apparel | Tea beverage | Body care |
| --- | --- | --- |
| ![Patagonia texture poster](examples/brand-source-studies/patagonia.png) | ![Quchashan texture poster](examples/brand-source-studies/quchashan.png) | ![Aesop texture poster](examples/brand-source-studies/aesop.png) |
| Sherpa fleece becomes a temporal terrain for “staying” | Milk foam and tea become the boundary where “landscape enters water” | Amber glass and bubbles become a vessel for everyday time |

| Consumer electronics | Sports nutrition |
| --- | --- |
| ![Bang & Olufsen texture poster](examples/brand-source-studies/bang-olufsen.png) | ![Maurten texture poster](examples/brand-source-studies/maurten.png) |
| The curvature of brushed aluminum gives form to invisible sound | Heat-sealed film and hydrogel express “enclose → pass through” |

For each study, see the [case index](examples/brand-source-studies/case-index.json) for the source page, direct URL, retained facts, deleted content, model-added content, and SHA-256. See [case-study notes](references/case-studies.md) for the translation decisions.

## Good and bad fits

Good fits: brand concept posters, product material narratives, cultural or nature themes, campaign key visuals, editorial covers, and photographic translations grounded in real surface evidence.

Bad fits: white-background e-commerce product images, product pages that must show every selling point, routine retouching or color grading, information-dense long graphics, and requests to imitate the composition of a specific reference.

## Input guidance

The most effective input usually includes:

- one high-resolution photograph with real surface detail;
- one communication objective rather than a list of style adjectives;
- the exact title, subtitle, and brand constraints that must appear;
- a clear instruction on whether the original object must remain recognizable.

When a low-resolution image proves only packaging or silhouette, the skill marks it as `structure-evidence` instead of pretending it contains usable microtexture.

## Quality bar

The visual master must pass five hard gates: communication, thumbnail, material irreplaceability, subtraction, and authenticity. The complete poster is scored on theme–material relationship, material dominance, abstract translation, editorial refinement, focal point, image–type integration, color and light unity, and distinctiveness. Only work scoring at least 80/100 is treated as final.

See [quality gates](references/quality-gates.md).

## Structure

```text
texture-poster-skill/
├── SKILL.md
├── README.md
├── README.en.md
├── artifact-template.json
├── agents/openai.yaml
├── assets/
│   ├── reference.png          # Style board composed of nine benchmark posters
│   └── preview.png
├── references/
│   ├── creative-brief.md
│   ├── art-direction.md
│   ├── generation-workflow.md
│   ├── source-and-rights.md
│   ├── quality-gates.md
│   └── case-studies.md
├── examples/brand-source-studies/
│   ├── source-to-poster-contact-sheet.png
│   ├── case-index.json
│   └── *.png                  # Five finished posters
└── scripts/validate_package.py
```

## Validation

Validate the package structure, case index, README image links, and output dimensions:

```powershell
python scripts/validate_package.py
```

The script uses only the Python standard library. It verifies that all five posters are `1122×1402` and the contact sheet is `2200×3100`.

## Usage boundaries

The five brand studies in this package use images from public web pages for internal, unofficial, transformative testing. Public availability does not grant commercial rights. Before formal publication, use a brand-authorized press kit, user-owned photography, or explicitly licensed imagery, and verify trademark, likeness, and derivative-use permissions.
