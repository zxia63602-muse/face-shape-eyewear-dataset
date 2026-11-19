# Face Shape Biometric Benchmarks & Optical Fit Dataset

Open dataset and deterministic calculator for facial anthropometry, face shape classification ratios, and optical eyewear sizing benchmarks.

Maintained as an open-source reference companion to [Face Shape Lens](https://faceshapelens.com), documenting the operational measurement criteria used by the site's face shape detection tool and optical fitting rules.

## Included Datasets & Tools

- **`data/face_shape_classification_benchmarks.csv`**: Anthropometric ratio intervals (Forehead-to-Cheekbone, Jaw-to-Cheekbone, and Length-to-Cheekbone) across 7 primary facial classifications (Oval, Round, Square, Heart, Diamond, Oblong, Triangle).
- **`data/eyewear_sizing_benchmarks.csv`**: Millimetre conversion matrix mapping lateral temple-to-temple facial breadth to hinge-to-hinge optical frame widths, bridge standards, and low-bridge clearance requirements.
- **`tools/eyewear_calculator.py`**: Standalone Python utility implementing the standard boxing calculation (`Total Width = 2 * Lens Width + Bridge Width`) and ratio-based shape classification.

## Data Source and Reproducibility

- **Classification Thresholds**: The anthropometric ratio intervals for the 7 primary face shapes are operational benchmarks defined by the Face Shape Lens detection tool.
- **Eyewear Sizing Matrix**: The eyewear size conversion table is derived directly from lateral facial breadth measurements calculated by the site.
- **Deterministic Reproducibility**: All classification and sizing calculations can be reproduced deterministically from numerical inputs using the included script (`tools/eyewear_calculator.py`). This repository makes no claim of reliance on external industry standards or third-party biometric databases.

## Optical Sizing Formula

Standard boxing specifications printed on the temple arm (`Eye □ DBL - Temple`) do not print total front width. Calculate total front clearance using:

```text
Total Frame Width (mm) = (2 × Lens Width) + Bridge Width (DBL)
```

Optician fitting allowance recommendation:
```text
Target Frame Width = Face Breadth (Temple to Temple) + 5 mm to 10 mm
```

This represents a dimensional conversion from stamped optical temple specifications; while the stamped markings follow general industry optical convention, the front clearance conversion formulas are implemented directly by this repository's script.

## Quick Start

Run the calculator with facial measurements in millimetres:

```bash
python tools/eyewear_calculator.py 190 130 120 108
```

## Citation & Reference

If you use this dataset or formula in optical sizing applications, please cite the source of this dataset from Face Shape Lens.

## License

MIT License. Open for public and commercial use.
