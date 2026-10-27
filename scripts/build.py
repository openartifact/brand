#!/usr/bin/env python3
# SPDX-FileCopyrightText: The OpenArtifact Authors
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Build every OpenArtifact logo SVG and PNG from the mark geometry and Inter outlines."""

import argparse
import os
import subprocess

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HDR = '<!--\nSPDX-FileCopyrightText: The OpenArtifact Authors\n\nSPDX-License-Identifier: CC-BY-SA-4.0\n-->\n'
PAD = 8  # lockup padding, keeps the lid's caps inside the canvas

# name: (frame, artifact, "Open", "Artifact")
VARIANTS = {
    'color': ('#4F46E5', '#818CF8', '#0F172A', '#4F46E5'),
    'color-dark': ('#818CF8', '#C7D2FE', '#F1F5F9', '#818CF8'),
    'black': ('#000', '#000', '#000', '#000'),
    'white': ('#FFF', '#FFF', '#FFF', '#FFF'),
}


class Text:
    def __init__(self, ttf_dir):
        self.fonts = {w: TTFont(os.path.join(ttf_dir, f'Inter-{w}.ttf')) for w in ('Medium', 'SemiBold')}

    def path(self, txt, weight, size, x, baseline, tracking=-0.02):
        """Outline txt; return (svg path data, x after the last glyph)."""
        font = self.fonts[weight]
        glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
        scale = size / font['head'].unitsPerEm
        parts = []
        for ch in txt:
            name = cmap[ord(ch)]
            pen = SVGPathPen(glyphs)
            glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, baseline)))
            parts.append(pen.getCommands())
            x += glyphs[name].width * scale + tracking * size
        return ' '.join(parts), x

    def wordmark(self, size, x, baseline, open_fill, artifact_fill):
        p1, x = self.path('Open', 'Medium', size, x, baseline)
        p2, x = self.path('Artifact', 'SemiBold', size, x, baseline)
        return f'<path d="{p1}" fill="{open_fill}"/><path d="{p2}" fill="{artifact_fill}"/>', x


def mark(frame, art, tx=0, ty=0, scale=1):
    return (
        f'<g transform="translate({tx} {ty}) scale({scale})">'
        f'<rect x="13" y="10" width="10" height="10" fill="{art}"/>'
        f'<path d="M5 11v15.25h22V11" fill="none" stroke="{frame}" stroke-width="3.5"/>'
        f'<path d="M3.5 9.5L13 3" fill="none" stroke="{frame}" stroke-width="3.5"/></g>'
    )


def svg(w, h, body, pad=0, bg=None):
    vb = f'{-pad} {-pad} {w + 2 * pad} {h + 2 * pad}'
    back = f'<rect x="{-pad}" y="{-pad}" width="{w + 2 * pad}" height="{h + 2 * pad}" fill="{bg}"/>' if bg else ''
    return (HDR + f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w + 2 * pad}" '
            f'height="{h + 2 * pad}"><title>OpenArtifact</title>{back}{body}</svg>\n')


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    return path


def png(src, width, out):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    subprocess.run(['rsvg-convert', '-w', str(width), src, '-o', out], check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inter', required=True, help='directory with Inter-Medium.ttf and Inter-SemiBold.ttf')
    text = Text(ap.parse_args().inter)
    out_png = os.path.join(ROOT, 'logo', 'png')

    for v, (frame, art, w1, w2) in VARIANTS.items():
        src = write(f'logo/mark/openartifact-mark-{v}.svg', svg(32, 32, mark(frame, art)))
        for w in (16, 32, 64, 128, 256, 512, 1024):
            png(src, w, os.path.join(out_png, f'openartifact-mark-{v}-{w}.png'))

        words, end = text.wordmark(44, 84, 50, w1, w2)
        src = write(f'logo/lockup/openartifact-horizontal-{v}.svg',
                    svg(int(end + 4), 64, mark(frame, art, 0, 0, 2) + words, PAD))
        for w in (512, 1024):
            png(src, w, os.path.join(out_png, f'openartifact-horizontal-{v}-{w}.png'))

        _, tw = text.wordmark(36, 0, 0, w1, w2)
        width = int(max(tw, 96) + 16)
        words, _ = text.wordmark(36, (width - tw) / 2, 146, w1, w2)
        src = write(f'logo/lockup/openartifact-stacked-{v}.svg',
                    svg(width, 160, mark(frame, art, (width - 96) / 2, 0, 3) + words, PAD))
        for w in (512, 1024):
            png(src, w, os.path.join(out_png, f'openartifact-stacked-{v}-{w}.png'))

    # GitHub social preview, 1280x640.
    _, tw = text.wordmark(96, 0, 0, '', '')
    gx = (1280 - (200 + tw)) / 2
    words, _ = text.wordmark(96, gx + 200, 358, '#F1F5F9', '#818CF8')
    tagline = 'Self-hosted, free-as-in-freedom artifact repository'
    _, lw = text.path(tagline, 'Medium', 30, 0, 0, 0)
    line, _ = text.path(tagline, 'Medium', 30, (1280 - lw) / 2, 470, 0)
    src = write('social/openartifact-social-dark.svg',
                svg(1280, 640, mark('#818CF8', '#C7D2FE', gx, 240, 5) + words + f'<path d="{line}" fill="#94A3B8"/>',
                    bg='#090B13'))
    png(src, 1280, os.path.join(ROOT, 'social', 'openartifact-social-dark.png'))


if __name__ == '__main__':
    main()
