"""I/O utilities for svgpython: conversion helpers."""
from pathlib import Path
from typing import Optional

def svg_to_pdf(svg_path: str | Path, pdf_path: Optional[str | Path] = None) -> Path:
    """Convert an SVG file to PDF using CairoSVG.

    Args:
        svg_path: path to source SVG file.
        pdf_path: path for output PDF. If None, same name as SVG with .pdf in same dir.

    Returns:
        Path to the created PDF file.
    """
    import shutil
    import subprocess

    svg_p = Path(svg_path)
    if pdf_path is None:
        pdf_p = svg_p.with_suffix('.pdf')
    else:
        pdf_p = Path(pdf_path)

    # Primary: try CairoSVG (pure-Python wrapper, but requires native cairo)
    try:
        import cairosvg  # type: ignore
        cairosvg.svg2pdf(url=str(svg_p), write_to=str(pdf_p))
        return pdf_p
    except Exception:
        # Fall through to external tools
        pass

    # Fallback 1: librsvg's rsvg-convert
    rsvg = shutil.which('rsvg-convert')
    if rsvg:
        cmd = [rsvg, '-f', 'pdf', '-o', str(pdf_p), str(svg_p)]
        subprocess.run(cmd, check=True)
        return pdf_p

    # Fallback 2: inkscape CLI (newer inkscape uses --export-type)
    inkscape = shutil.which('inkscape')
    if inkscape:
        # Try new CLI style first
        cmd = [inkscape, str(svg_p), '--export-type=pdf', f'--export-filename={str(pdf_p)}']
        res = subprocess.run(cmd)
        if res.returncode == 0:
            return pdf_p
        # Try legacy inkscape CLI
        cmd = [inkscape, '-o', str(pdf_p), str(svg_p)]
        subprocess.run(cmd, check=True)
        return pdf_p

    raise RuntimeError(
        "Could not convert SVG to PDF: CairoSVG failed and neither 'rsvg-convert' nor 'inkscape' were found."
        " Install cairo via Homebrew (`brew install cairo pango librsvg`) or install Inkscape,"
        " then retry."
    )
