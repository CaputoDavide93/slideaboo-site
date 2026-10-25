#!/usr/bin/env python3
"""Draw docs/assets/social-preview.png (1280x640) from the app icon in
assets/icon.png and the site's colour tokens. Metadata is stripped.

  make social
"""
from __future__ import annotations

import pathlib

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[2]
W, H = 1280, 640
BG, SURFACE, LINE = (15, 24, 38), (26, 38, 56), (43, 55, 72)       # dark --sky-top, --surface, --line
TEXT, MUTED, ACCENT = (232, 237, 242), (164, 175, 188), (140, 199, 191)
FONTS = ["/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/SFNS.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for path in FONTS:
        try:
            return ImageFont.truetype(path, size, index=1 if bold and path.endswith(".ttc") else 0)
        except OSError:
            continue
    return ImageFont.load_default()


def clean(im: Image.Image, path: pathlib.Path) -> None:
    """Save pixels only, so no text chunks or timestamps remain."""
    out = Image.new("RGB", im.size)
    out.putdata(list(im.convert("RGB").getdata()))
    out.save(path, optimize=True)


def main() -> None:
    icon = Image.open(ROOT / "assets" / "icon.png").convert("RGB").resize((200, 200), Image.LANCZOS).convert("RGBA")
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    mask = Image.new("L", (200, 200), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, 199, 199], 44, fill=255)
    im.paste(icon, (96, 96), mask)
    d.text((96, 330), "Slideaboo site", font=font(80, True), fill=TEXT)
    d.text((96, 436), "Privacy policy and contact pages for a", font=font(36), fill=MUTED)
    d.text((96, 484), "toddler puzzle app that keeps everything on the device.", font=font(36), fill=MUTED)
    x = 96
    for chip in ("Privacy policy", "English and Italian", "No scripts or cookies", "Static HTML"):
        f = font(26)
        w = d.textlength(chip, font=f)
        d.rounded_rectangle([x, 548, x + w + 40, 596], 24, fill=SURFACE, outline=LINE)
        d.text((x + 20, 560), chip, font=f, fill=ACCENT)
        x += w + 40 + 16
    clean(im, ROOT / "docs" / "assets" / "social-preview.png")
    print("wrote docs/assets/social-preview.png")


if __name__ == "__main__":
    main()
