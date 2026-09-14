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

After installation, attach a source image and brief the agent as you would in a real design commission: state the business objective, audience, channel, communication theme, exact copy, and brand constraints. The skill should decide the material selection, visual subtraction, and translation method.

### 1. Outdoor apparel: repair-and-reuse campaign

```text
The attachment is a product image of an older sherpa-fleece jacket. Use $texture-poster-skill to create a 4:5 social teaser for our autumn repair-and-reuse program.
The audience is existing outerwear customers aged 25–40 who care about durability and environmental impact. The message is not about saving money; it is about allowing a garment to continue accompanying its owner. Use the title “STAY” and the subtitle “Warmth does not have to begin with new.” Keep the tone restrained rather than preachy.
```

### 2. Tea beverage: regional product teaser

```text
The attachment is a product image of a new milk-foam tea. Use $texture-poster-skill to create a pre-launch poster for a regional limited edition, distributed through our official account and lifestyle social channels.
Urban customers should sense a connection between the ingredients and a mountain region, without a literal mountain illustration or an ingredient list. Use “LANDSCAPE IN WATER” as the title and “The mountain reaches the cup in another form” as the subtitle. Vertical 4:5; appetizing, but not a promotional menu.
```

### 3. Body care: member-magazine cover

```text
The attachment is a product image of our amber-glass body-care range. Use $texture-poster-skill to create a 4:5 editorial cover for the member magazine's “Daily Care” feature.
Readers already know the product, so this is not an e-commerce selling-point page. Communicate the idea that repeated daily actions can gradually change time. Use “RENEWAL” as the title. Keep the result quiet, restrained, and consistent with the brand's rational tone.
```

### 4. Consumer audio: launch-event key visual

```text
The attachment is a product image of an upcoming aluminum home speaker. Use $texture-poster-skill to create a 4:5 key visual for the launch announcement and social campaign.
The audience is design professionals and premium-audio customers. The message is that sound has no visible form but leaves direction in space. Use “GIVE FORM” as the title and “A shape for what cannot be seen” as the subtitle. The result should feel premium and precise, not like a specification sheet.
```

### 5. Sports nutrition: long-distance training feature

```text
The attachment is a product image of our energy-gel pack. Use $texture-poster-skill to create a 4:5 content cover for a marathon training program's feature on fueling timing.
The audience is runners targeting a three-to-five-hour finish. Do not emphasize discounts or flavors. The core message is that energy is carried reliably and released when the body needs it. Use “THROUGH” as the title and “Energy for the next stretch” as the subtitle. The visual should feel active without relying on conventional speed lines.
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
