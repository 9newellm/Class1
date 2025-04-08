# Python script to compare a given experimental wavelength to theoretical wavelengths for Na-S lines

import numpy as np
from FormatConfig import *
import pandas as pd

def classify_wavelength(wavelength):
    """
    Classifies a given wavelength (in nm) into its corresponding region 
    in the electromagnetic spectrum.
    """
    if wavelength < 10:
        return "X-rays or Gamma rays"
    elif 10 <= wavelength < 400:
        return "Ultraviolet (UV)"
    elif 400 <= wavelength < 700:
        return "Visible Light"
    elif 700 <= wavelength < 1000000:  # 1 mm = 1,000,000 nm
        return "Infrared (IR)"
    elif 1000000 <= wavelength < 1000000000:  # 1 m = 1,000,000,000 nm
        return "Microwaves"
    else:
        return "Radio Waves"

# Example usage:
wavelength_nm = 589  # Example for Sodium D-line
spectrum_region = classify_wavelength(wavelength_nm)
print(f"The wavelength {wavelength_nm} nm falls in the {spectrum_region} region.")


"""
Documented Notes: 

Na-S Lines refer to specific transitions in the sodium atom (Na), but not in the D-line region. These lines are related to forbidden transitions that occur in certain conditions (like in high-energy states or specific ionized states).

The Na-S lines are part of SampleTypes_Notes/Part 0. Effective Z. Understanding_Fundamental_Physics_Behind_Effective_Z.docx SampleTypes_Notes/Part 1. Effective_Z_and_Quantum_Defect_Explanation.docx SampleTypes_Notes/Part 2. (Effective Z___) Spectral_Imaging_Experiment_Na_Doublet.docxthe sodium spectrum, particularly in the ultraviolet (UV) or near-infrared regions. These lines are connected to the transitions involving the sodium atom in the S-shell, typically the 3^2S level.

In sodium (Na), the Na-S lines generally involve transitions between these states:

Na (3^2S) → higher excited states: The 3^2S state is often involved in forbidden transitions that give rise to specific spectral lines in the ultraviolet or infrared range.

Because these transitions are forbidden or weak, they are more challenging to detect compared to the more common D-lines. They are less intense and may be visible only under specific experimental conditions, such as low-pressure sodium vapor lamps or in controlled laboratory settings.

Common Na-S Lines:
Na (3^2S1/2 → 3^2P1/2): In the UV range, but typically much weaker than the more prominent D-line emissions."""

### User defined inputs. 
EXPERIMENTALwAVELENGTHoBTINAED = 800.56  # Example wavelength (e.g., 589.56 nm, Na-D2)

### System Constants
Z_SODIUM = 11
Z_EFFECTIVE = 1 # (Tennyson Equation 6.1)
R_H = 1.097373e7  # Rydberg constant in m^-1
R_H = R_H * 10**(-9)

# Function to calculate theoretical wavelengths for Na-S lines
def calculate_theoretical_wavelengths(n1, n_max=10, Z=1):
    """
    Calculate theoretical wavelengths for transitions from n_max to n1 (e.g., n1 = 3 for Na-S lines).
    """
    wavelengths, wavelengthClassification = [], []
    for n2 in range(n_max, n1, -1):  # From n_max to n1
        wavelength = 1 / (R_H * Z**2 * (1/n1**2 - 1/n2**2))  # Using Rydberg formula
        wavelengths.append(wavelength)  # Convert from meters to nm
        wavelengthClassification = classify_wavelength(wavelength) # must be in nm
    return wavelengths, wavelengthClassification

# Function to compare experimental wavelength with theoretical wavelengths
def compare_wavelengths(experimental_wavelength, n1=3, n_max=10, Z_Choice=1):
    """
    Compare the experimental wavelength with theoretical wavelengths for Na-S lines
    """
    theoretical_wavelengths, classify = calculate_theoretical_wavelengths(n1, n_max, Z=Z_Choice)
    
    print("Experimental wavelength:", experimental_wavelength, "nm")
    print("Theoretical wavelengths for Na-S lines (n -> 3):")
    for n2, theoretical_wavelength in zip(range(n_max, n1, -1), theoretical_wavelengths):
        print(f"Transition from n={n2} to n={n1}: {theoretical_wavelength:.2f} nm")
        
    # Find the closest theoretical wavelength
    closest_theoretical = min(theoretical_wavelengths, key=lambda x: abs(x - experimental_wavelength))
    closest_index = theoretical_wavelengths.index(closest_theoretical)
    closest_n2 = n_max - closest_index

    print(f"\nClosest theoretical wavelength: {closest_theoretical:.2f} nm (n={closest_n2} to n={n1})")

        # Create a dictionary to store the data
    data = {
    "Theoretical Wavelengths (nm)": theoretical_wavelengths,
    "Z":Z_Choice, 
    "classifications": classify}

    return pd.DataFrame(data)

if __name__ == "__main__":
    print(LINE_UNDERSCORE_HOLD_MAIN_15)
    print("LOOKING AT THE EFFECTIVE Z FOR SODIUM. Before considering external impact.")
    set1 = compare_wavelengths(EXPERIMENTALwAVELENGTHoBTINAED, n1=3, n_max=21, Z_Choice=Z_SODIUM)  # n1=3 corresponds to Na-S lines
    print(LINE_UNDERSCORE_HOLD_MAIN_15)

    print(LINE_UNDERSCORE_HOLD_MAIN_15)
    print("LOOKING AT THE EFFECTIVE Z FOR HYDROGEN.")
    set2 =  compare_wavelengths(EXPERIMENTALwAVELENGTHoBTINAED, n1=3, n_max=21, Z_Choice=Z_EFFECTIVE)  # n1=3 corresponds to Na-S lines
    print(LINE_UNDERSCORE_HOLD_MAIN_15)

        # Subtract corresponding columns
    df_diff = set1["Theoretical Wavelengths (nm)"] - set2["Theoretical Wavelengths (nm)"]  # Or use df1.sub(df2)
    df_abs_diff = df_diff.abs()

    print(LINE_UNDERSCORE_HOLD_MAIN_15)
    print("Displaying the difference between two different z-sets")
    # Display the result
    print(df_abs_diff)
    ## Range of wavelengths (display them to show the user). 
    print(set1["classifications"])

    ## Range of wavelengths (display them to show the user). 
    print(set2["classifications"])
