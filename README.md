# Face Shape Biometric Benchmarks & Optical Fit Dataset

Open dataset and deterministic calculator for facial anthropometry, face shape classification ratios, and optical eyewear sizing benchmarks.

Maintained as an open-source reference companion to [Face Shape Lens](https://faceshapelens.com), documenting verified measurement criteria and optician bench rules.

## Included Datasets & Tools

- **`data/face_shape_classification_benchmarks.csv`**: Anthropometric ratio intervals (Forehead-to-Cheekbone, Jaw-to-Cheekbone, and Length-to-Cheekbone) across 7 primary facial classifications (Oval, Round, Square, Heart, Diamond, Oblong, Triangle).
- **`data/eyewear_sizing_benchmarks.csv`**: Millimetre conversion matrix mapping lateral temple-to-temple facial breadth to hinge-to-hinge optical frame widths, bridge standards, and low-bridge clearance requirements.
- **`tools/eyewear_calculator.py`**: Standalone Python utility implementing the standard boxing calculation (`Total Width = 2 * Lens Width + Bridge Width`) and ratio-based shape classification.

## Optical Sizing Formula

Standard boxing specifications printed on the temple arm (`Eye □ DBL - Temple`) do not print total front width. Calculate total front clearance using:

```text
Total Frame Width (mm) = (2 × Lens Width) + Bridge Width (DBL)
```

Optician fitting allowance recommendation:
```text
Target Frame Width = Face Breadth (Temple to Temple) + 5 mm to 10 mm
```

## Quick Start

Run the calculator with facial measurements in millimetres:

```bash
python tools/eyewear_calculator.py 190 130 120 108
```

## Citation & Reference

If you use this dataset or formula in optical sizing applications, please cite the underlying standards from [Face Shape Lens](https://faceshapelens.com).

## License

MIT License. Open for public and commercial use.
