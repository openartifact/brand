<!--
SPDX-FileCopyrightText: The OpenArtifact Authors

SPDX-License-Identifier: CC-BY-SA-4.0
-->

<p align="center">
  <img src="logo/lockup/openartifact-horizontal-color.svg" alt="OpenArtifact" width="420">
</p>

# OpenArtifact brand

Logos, colours and type for [OpenArtifact](https://github.com/openartifact/openartifact). This repository is the source of truth; the product repo keeps only the copies it ships (favicon, in-app mark, README logo).

## Mark

The "open crate": a crate with its lid swung open and an artifact rising out. Drawn on a 32×32 grid so it stays crisp at 16 px.

| Variant | SVG | Use |
|---|---|---|
| Colour | [`openartifact-mark-color.svg`](logo/mark/openartifact-mark-color.svg) | Default, light backgrounds |
| Colour, dark | [`openartifact-mark-color-dark.svg`](logo/mark/openartifact-mark-color-dark.svg) | Dark backgrounds |
| Black | [`openartifact-mark-black.svg`](logo/mark/openartifact-mark-black.svg) | One-colour print, light backgrounds |
| White | [`openartifact-mark-white.svg`](logo/mark/openartifact-mark-white.svg) | On the primary colour or photos |

## Lockups

The wordmark is "Open" in Inter Medium plus "Artifact" in Inter SemiBold, tracking −0.02 em, "Artifact" in the primary colour. Text is outlined, so no font is needed to display the files.

| | Horizontal | Stacked |
|---|---|---|
| Colour | [svg](logo/lockup/openartifact-horizontal-color.svg) | [svg](logo/lockup/openartifact-stacked-color.svg) |
| Colour, dark | [svg](logo/lockup/openartifact-horizontal-color-dark.svg) | [svg](logo/lockup/openartifact-stacked-color-dark.svg) |
| Black | [svg](logo/lockup/openartifact-horizontal-black.svg) | [svg](logo/lockup/openartifact-stacked-black.svg) |
| White | [svg](logo/lockup/openartifact-horizontal-white.svg) | [svg](logo/lockup/openartifact-stacked-white.svg) |

PNG exports (transparent) are in [`logo/png/`](logo/png): marks at 16–1024 px, lockups at 512 and 1024 px wide. [`social/`](social) has the 1280×640 repository social preview.

### Usage

- Keep clear space of at least the artifact square's width around the mark.
- Minimum size: mark 16 px, horizontal lockup 120 px wide.
- Don't recolour outside the variants above, rotate, stretch, add effects (shadows, gradients, glows), or re-set the wordmark in another font.
- Write the name as **OpenArtifact**: one word, capital O and A.

## Colour

| Token | Light | Dark |
|---|---|---|
| Primary (mark frame, "Artifact") | `#4F46E5` | `#818CF8` |
| Accent (artifact square) | `#818CF8` | `#C7D2FE` |
| Background | `#F9FAFB` | `#090B13` |
| Surface | `#FFFFFF` | `#111420` |
| Foreground | `#111827` | `#EBEEF5` |
| Muted | `#6B7280` | `#94A3B8` |
| Border | `#E5E7EB` | `#242A3A` |
| Success | `#166534` | `#86EFAC` |
| Warning | `#854D0E` | `#FACC15` |
| Danger | `#991B1B` | `#F87171` |

Charts use a separate 12-colour categorical palette. All values, including the soft variants, are in [`tokens/tokens.json`](tokens/tokens.json) and as CSS custom properties in [`tokens/tokens.css`](tokens/tokens.css). They mirror `web/src/style.css` and `web/src/lib/formats.ts` in the product repo; change both together.

## Type

- **Inter** for UI and the wordmark; **JetBrains Mono** for code, versions and repository names.
- Both are under the SIL Open Font License and are not redistributed here: get them from [rsms.me/inter](https://rsms.me/inter/) and [jetbrains.com/lp/mono](https://www.jetbrains.com/lp/mono/).

## Style

Flat and quiet: solid colours, thin borders, no gradients, glows, blur or letter-spaced uppercase labels. Show real data; skip decoration.

## Regenerating

`scripts/build.py` writes every SVG and PNG from the mark geometry and Inter's outlines:

```sh
pip install fonttools
python3 scripts/build.py --inter /path/to/Inter-4.1/extras/ttf   # needs rsvg-convert
```

## License

Artwork and documentation: [CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt). Build script: [AGPL-3.0-or-later](LICENSES/AGPL-3.0-or-later.txt).

The OpenArtifact name and logo identify the official project. The licence covers copyright only; it does not grant trademark rights. You may use them to refer to OpenArtifact, but not in a way that suggests endorsement, or as the name or logo of a fork or another product.
