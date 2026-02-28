#!/usr/bin/env python3
"""Example: draw three red circles, save SVG & PDF, and display ASCII preview in terminal."""
from __future__ import annotations

from pathlib import Path
import svgwrite

from svgpython.io import svg_to_pdf


def make_svg(svg_path: Path) -> Path:
    dwg = svgwrite.Drawing(filename=str(svg_path), size=(400, 200))
    # three red filled circles
    dwg.add(dwg.circle(center=(80, 100), r=40, fill='red'))
    dwg.add(dwg.circle(center=(200, 100), r=40, fill='red'))
    dwg.add(dwg.circle(center=(320, 100), r=40, fill='red'))
    dwg.save()
    return svg_path


def ascii_preview(png_path: Path, width: int = 80) -> None:
    try:
        from PIL import Image
    except Exception:
        print("Pillow not available — skipping ASCII preview")
        return

    img = Image.open(png_path).convert('L')
    w, h = img.size
    aspect = h / w
    new_w = width
    new_h = max(1, int(aspect * new_w * 0.5))
    img = img.resize((new_w, new_h))
    pixels = img.getdata()
    chars = " .:-=+*#%@"
    out = ""
    for y in range(new_h):
        row = ""
        for x in range(new_w):
            row += chars[pixels[y * new_w + x] * (len(chars) - 1) // 255]
        out += row + "\n"
    print(out)


def main() -> None:
    base = Path.cwd()
    svgs = base / 'svgs'
    svgs.mkdir(exist_ok=True)

    svg_path = svgs / 'three_circles.svg'
    pdf_path = svgs / 'three_circles.pdf'
    png_path = svgs / 'three_circles.png'

    print(f"Creating SVG: {svg_path}")
    make_svg(svg_path)

    print(f"Converting to PDF: {pdf_path}")
    svg_to_pdf(svg_path, pdf_path)

    # Try to produce a PNG for terminal preview using cairosvg
    try:
        import cairosvg
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path))
        print(f"Produced PNG preview: {png_path}")
        ascii_preview(png_path)
    except Exception as e:
        print("Could not produce PNG preview:", e)

    print("Done. Files:")
    print(" - SVG:", svg_path)
    print(" - PDF:", pdf_path)


if __name__ == '__main__':
    main()
