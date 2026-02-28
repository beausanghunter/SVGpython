#!/usr/bin/env python3
"""Example: draw three red circles, save SVG & PDF, and display ASCII preview in terminal."""
from __future__ import annotations

from pathlib import Path
import svgwrite

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from svgpython.io import svg_to_pdf


def make_svg(svg_path: Path) -> Path:
    width = 400
    height = 200
    dwg = svgwrite.Drawing(filename=str(svg_path), size=(f"{width}px", f"{height}px"), viewBox=f"0 0 {width} {height}")
    # off-white background (use absolute size so it fills the whole canvas)
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='#f8f7f2'))

    # three red filled circles
    dwg.add(dwg.circle(center=(80, 100), r=40, fill='red'))
    dwg.add(dwg.circle(center=(200, 100), r=40, fill='red'))
    dwg.add(dwg.circle(center=(320, 100), r=40, fill='red'))
    dwg.save()
    return svg_path


from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication
import sys


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

    # Display the SVG graphically using PyQt5
    try:
        app = QApplication(sys.argv)
        svg_widget = QSvgWidget(str(svg_path))
        svg_widget.setWindowTitle('Three Red Circles')
        svg_widget.resize(600, 300)
        svg_widget.show()
        app.exec_()
    except Exception as e:
        print('Could not display SVG (PyQt5 may not be available or running headless):', e)

    print("Done. Files:")
    print(" - SVG:", svg_path)
    print(" - PDF:", pdf_path)


if __name__ == '__main__':
    main()
