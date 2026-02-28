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
    try:
        import cairosvg
    except Exception as e:
        raise RuntimeError("cairosvg is required for svg_to_pdf — install via pip: cairosvg") from e

    svg_p = Path(svg_path)
    if pdf_path is None:
        pdf_p = svg_p.with_suffix('.pdf')
    else:
        pdf_p = Path(pdf_path)

    cairosvg.svg2pdf(url=str(svg_p), write_to=str(pdf_p))
    return pdf_p
