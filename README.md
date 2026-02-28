# SVGpython

This repository contains utilities for generating SVG shapes (ovoids, bezier curves) and small viewer scripts.

Quick start

1. Create virtual environment: `python3 -m venv .venv`
2. Activate it: `source .venv/bin/activate`
3. Install deps: `pip install -r requirements.txt`
4. Run examples like `python3 svgOvoid.py` or `python3 SVGviewer.py`

**CLI: convert SVG → PDF**

A small helper script is provided to convert SVG files to PDF using CairoSVG.

- Convert an SVG to PDF (venv activated):

```bash
python scripts/svg2pdf.py svgs/svgwrite-example.svg
```

- Convert the example output produced by an example script:

```bash
python examples/svgOvoid.py
python scripts/svg2pdf.py svgs/svgwrite-example6.svg
```

Or call the converter from Python:

```py
from svgpython.io import svg_to_pdf
svg_to_pdf('svgs/svgwrite-example.svg')
```

