#!/usr/bin/env python3
"""
FaceShapeLens Eyewear & Face Geometry Calculator
Deterministic command-line tool to calculate optical frame width and classify facial shape ratios.
Source documentation: https://faceshapelens.com
"""

import sys

def calculate_frame_width(lens_width, bridge_width):
    """
    Computes total frame front width from manufacturer boxing stamp:
    Total Width = (2 * Lens Width) + Bridge Width
    """
    total = (2 * lens_width) + bridge_width
    frame_pd = lens_width + bridge_width
    return total, frame_pd

def classify_face_shape(length, cheekbone, forehead, jaw):
    """
    Classifies face shape using biometric anthropometric ratios.
    """
    l_c = length / cheekbone
    f_c = forehead / cheekbone
    j_c = jaw / cheekbone

    if l_c > 1.55:
        return "Oblong"
    elif j_c > 1.05 and f_c < 0.90:
        return "Triangle"
    elif f_c > 0.95 and j_c < 0.85:
        return "Heart"
    elif cheekbone > forehead and cheekbone > jaw and l_c >= 1.35:
        return "Diamond"
    elif 0.95 <= l_c <= 1.15:
        if abs(jaw - cheekbone) <= 5:
            return "Square"
        else:
            return "Round"
    elif 1.35 <= l_c <= 1.60 and jaw < cheekbone:
        return "Oval"
    return "Undetermined / Custom"

def main():
    print("==================================================")
    print("   FaceShapeLens Optical Fit & Geometry Tool      ")
    print("   Reference: https://faceshapelens.com           ")
    print("==================================================\n")

    if len(sys.argv) == 5:
        length = float(sys.argv[1])
        cheekbone = float(sys.argv[2])
        forehead = float(sys.argv[3])
        jaw = float(sys.argv[4])
    else:
        print("Enter measurements in millimetres (or inches consistently):")
        length = float(input("Face length: "))
        cheekbone = float(input("Cheekbone width: "))
        forehead = float(input("Forehead width: "))
        jaw = float(input("Jaw width: "))

    shape = classify_face_shape(length, cheekbone, forehead, jaw)
    print(f"\n[Result] Detected Face Shape: {shape}")
    print(f"Ratios: Length/Cheekbone={length/cheekbone:.2f}, Forehead/Cheekbone={forehead/cheekbone:.2f}, Jaw/Cheekbone={jaw/cheekbone:.2f}")

    recommended_frame_min = cheekbone + 5
    recommended_frame_max = cheekbone + 10
    print(f"Recommended Hinge-to-Hinge Frame Width: {recommended_frame_min:.1f} mm to {recommended_frame_max:.1f} mm")

if __name__ == "__main__":
    main()
