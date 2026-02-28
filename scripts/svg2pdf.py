#!/usr/bin/env python3
"""Simple CLI to convert an SVG file to PDF using svgpython.io.svg_to_pdf."""
from __future__ import annotations

import argparse
from pathlib import Path
from svgpython.io import svg_to_pdf


def main() -> None:
    p = argparse.ArgumentParser(description="Convert SVG to PDF using svgpython")
    p.add_argument("svg", help="Path to input SVG file")
    p.add_argument("-o", "--out", help="Path to output PDF file (optional)")
    args = p.parse_args()

    svg_path = Path(args.svg)
    if not svg_path.exists():
        raise SystemExit(f"Input SVG not found: {svg_path}")

    out_path = Path(args.out) if args.out else None
    pdf_path = svg_to_pdf(svg_path, out_path)
    print(f"Wrote PDF: {pdf_path}")


if __name__ == "__main__":
    main()
