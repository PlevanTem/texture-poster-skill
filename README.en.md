<div align="center">

# Texture Poster

**A texture-driven editorial poster skill**

Transform an ordinary photograph, product image, or brand theme into an editorial poster where real material texture carries the concept.

[简体中文](README.md) · [English](README.en.md)

[![GitHub Stars](https://img.shields.io/github/stars/PlevanTem/texture-poster-skill?style=social)](https://github.com/PlevanTem/texture-poster-skill/stargazers)
![WeChat lelouchdbf](https://img.shields.io/badge/WeChat-lelouchdbf-07C160?style=flat-square&logo=wechat&logoColor=white)

</div>

This is not a tool for placing a texture overlay on a photograph. It removes irrelevant context first, then uses material texture, scale, light, negative space, and precise typography to communicate an indirect association.

![Five brand source-to-texture-poster studies](examples/brand-source-studies/source-to-poster-contact-sheet.png)

## Installation

### Method 1: use [`npx skills`](https://github.com/vercel-labs/skills) (recommended)

Install globally for both Codex and Claude Code:

```bash
npx skills add PlevanTem/texture-poster-skill --global --agent codex --agent claude-code --copy --yes
```

If you use only one agent, remove the other `--agent` option. Start a new session after installation so the agent can discover the skill.

### Method 2: install manually

1. Download and extract the repository ZIP. Make sure `SKILL.md` sits directly inside the extracted skill folder.
2. Copy the complete `texture-poster-skill` folder to the appropriate location:

| Agent | Windows | macOS / Linux |
| --- | --- | --- |
| Codex | `C:\Users\<username>\.codex\skills\texture-poster-skill` | `~/.codex/skills/texture-poster-skill` |
| Claude Code | `C:\Users\<username>\.claude\skills\texture-poster-skill` | `~/.claude/skills/texture-poster-skill` |

3. Start a new session and invoke `$texture-poster-skill`.

## Quick start

After installation, attach a source image and send one of these realistic tasks to your agent. Replace the copy, aspect ratio, and brand constraints as needed.

### 1. Outdoor apparel: turn fabric into temporal terrain

```text
Use $texture-poster-skill on the attached sherpa-fleece jacket image to create a 4:5 campaign poster for a repair-and-reuse program.
Keep the fleece, binding, and a short section of zipper teeth. Remove the full garment, pockets, logo, and white background. The theme is “STAY”; use the headline “Warmth does not have to begin with new.”
```

### 2. Tea beverage: suggest origin through a liquid boundary

```text
Use $texture-poster-skill to turn the attached milk-foam tea photograph into a product teaser poster.
Do not show the complete cup or store. Enlarge the foam folds, tea boundary, and a few ingredients. Use “LANDSCAPE IN WATER” as the title and “The mountain reaches the cup in another form” as the subtitle. Vertical 4:5.
```

### 3. Body care: express everyday time through a container

```text
Use $texture-poster-skill on the attached amber-glass body-care bottle to create an editorial cover for a member magazine.
Keep the glass thickness, internal dark axis, bubbles, and refracted edge. Remove the pump, label, and complete bottle silhouette. The theme is “RENEWAL”; keep the result restrained and quiet rather than presenting a conventional product shot.
```

### 4. Consumer audio: let material give sound a shape

```text
Use $texture-poster-skill to turn the attached aluminum speaker image into a launch-event key visual.
Keep only the brushed-metal direction, conical curvature, and a small area of acoustic grooves. Add one restrained interference deformation to imply resonance. Use the title “GIVE FORM”; remove the complete speaker silhouette and brand logo.
```

### 5. Sports nutrition: turn package structure into an energy path

```text
Use $texture-poster-skill on the attached energy-gel pack to make a 4:5 poster for a long-distance training feature.
Use the black film, heat-seal folds, and narrow opening as source facts. Introduce translucent hydrogel and a few warm particles to express “enclose → pass through.” Use the title “THROUGH” and avoid showing the complete package.
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

## Use cases

| Use case | What the skill is suited to solve |
| --- | --- |
| Brand concept posters | Express a brand proposition through physical material behavior instead of direct product display |
| Product launches and campaign key visuals | Extract one recognizable visual motif from a source product image |
| Product texture narratives | Magnify real evidence from fabric, glass, metal, liquid, film, and other surfaces |
| Editorial covers and social content | Build one focal point and a clear light–dark structure at phone-thumbnail size |
| Cultural and nature themes | Translate terrain, architecture, plants, or craft materials into indirect conceptual associations |

It is not intended for white-background e-commerce images, routine retouching, information-dense long graphics, or copying the specific composition of a benchmark poster.

## Input guidance

The most effective input usually includes:

- one high-resolution photograph with real surface detail;
- one communication objective rather than a list of style adjectives;
- the exact title, subtitle, and brand constraints that must appear;
- a clear instruction on whether the original object must remain recognizable.

When a low-resolution image proves only packaging or silhouette, the skill marks it as `structure-evidence` instead of pretending it contains usable microtexture.

## Quality bar

| Hard gate | Pass condition | Failure signal |
| --- | --- | --- |
| Visual communication | Cropping, scale, light, tonal range, depth, and visual movement already make the image feel deliberately designed | It remains an ordinary photograph, a uniform filter, or a background waiting for text to rescue it |
| Thumbnail | At phone-preview size, one focal point and a clear large-scale light–dark relationship remain | Multiple focal points compete and the first look has no direction |
| Material irreplaceability | The material's physical property directly expresses the theme; replacing it would damage the concept | Paper, stone, metal, or water could be exchanged without changing the idea |
| Subtraction | When object recognition is unnecessary, roughly 50%–70% of the surrounding scene has been removed or reorganized | Product and context remain almost untouched beneath typography and noise |
| Authenticity | Scale, direction, light, roughness, and spatial depth feel physically credible | Tiled texture, repeated noise, or plastic CGI appearance |

All five gates must pass. A complete poster must also score at least 80/100 before it is treated as final.

See [quality gates](references/quality-gates.md).

## Structure

```text
texture-poster-skill/
├── SKILL.md                       # Primary agent instructions and core contract
├── README.md                      # Chinese documentation
├── README.en.md                   # English documentation
├── artifact-template.json         # Image-template type, reference, and preview declaration
├── agents/
│   └── openai.yaml                # Display name, icon, default prompt, and invocation policy
├── assets/
│   ├── reference.png              # Nine-poster style board, not a layout template
│   └── preview.png                # Skill-list and gallery preview
├── references/
│   ├── creative-brief.md           # Pre-generation concept and material brief
│   ├── art-direction.md            # Material, light, color, and invisible-grid method
│   ├── generation-workflow.md      # Text-free master, typesetting, review, and delivery
│   ├── source-and-rights.md        # Source records and commercial-use boundaries
│   ├── quality-gates.md            # Five hard gates, scoring rubric, and failure fixes
│   └── case-studies.md             # Translation notes for the five brand studies
├── examples/
│   └── brand-source-studies/
│       ├── source-to-poster-contact-sheet.png  # Five source-to-poster comparisons
│       ├── case-index.json                    # Sources, decisions, additions, and file checks
│       └── *.png                              # Five finished posters
└── scripts/
    └── validate_package.py          # Internal package and case validation run by the agent
```

## Usage boundaries

The five brand studies in this package use images from public web pages for internal, unofficial, transformative testing. Public availability does not grant commercial rights. Before formal publication, use a brand-authorized press kit, user-owned photography, or explicitly licensed imagery, and verify trademark, likeness, and derivative-use permissions.
