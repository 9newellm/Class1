# Python script to compare a given experimental wavelength to theoretical wavelengths for Na-S lines

import numpy as np


EXPERIMENTALwAVELENGTHoBTINAED = 589.56  # Example wavelength (e.g., 589.56 nm, Na-D2)
SODIUM_Z = 11

"""Na-S Lines refer to specific transitions in the sodium atom (Na), but not in the D-line region. These lines are related to forbidden transitions that occur in certain conditions (like in high-energy states or specific ionized states).

The Na-S lines are part of the sodium spectrum, particularly in the ultraviolet (UV) or near-infrared regions. These lines are connected to the transitions involving the sodium atom in the S-shell, typically the 3^2S level.

In sodium (Na), the Na-S lines generally involve transitions between these states:

Na (3^2S) → higher excited states: The 3^2S state is often involved in forbidden transitions that give rise to specific spectral lines in the ultraviolet or infrared range.

Because these transitions are forbidden or weak, they are more challenging to detect compared to the more common D-lines. They are less intense and may be visible only under specific experimental conditions, such as low-pressure sodium vapor lamps or in controlled laboratory settings.

Common Na-S Lines:
Na (3^2S1/2 → 3^2P1/2): In the UV range, but typically much weaker than the more prominent D-line emissions."""

# Constants
R_H = 1.097373e7  # Rydberg constant in m^-1
R_H = R_H * 10**(-9)
print(R_H)
# Function to calculate theoretical wavelengths for Na-S lines
def calculate_theoretical_wavelengths(n1, n_max=10):
    """
    Calculate theoretical wavelengths for transitions from n_max to n1 (e.g., n1 = 3 for Na-S lines).
    """
    wavelengths = []
    for n2 in range(n_max, n1, -1):  # From n_max to n1
        wavelength = 1 / (R_H * SODIUM_Z**2 * (1/n1**2 - 1/n2**2))  # Using Rydberg formula
        wavelengths.append(wavelength)  # Convert from meters to nm
    return wavelengths

# Function to compare experimental wavelength with theoretical wavelengths
def compare_wavelengths(experimental_wavelength, n1=3, n_max=10):
    """
    Compare the experimental wavelength with theoretical wavelengths for Na-S lines
    """
    theoretical_wavelengths = calculate_theoretical_wavelengths(n1, n_max)
    
    print("Experimental wavelength:", experimental_wavelength, "nm")
    print("Theoretical wavelengths for Na-S lines (n -> 3):")
    for n2, theoretical_wavelength in zip(range(n_max, n1, -1), theoretical_wavelengths):
        print(f"Transition from n={n2} to n={n1}: {theoretical_wavelength:.2f} nm")
        
    # Find the closest theoretical wavelength
    closest_theoretical = min(theoretical_wavelengths, key=lambda x: abs(x - experimental_wavelength))
    closest_index = theoretical_wavelengths.index(closest_theoretical)
    closest_n2 = n_max - closest_index

    print(f"\nClosest theoretical wavelength: {closest_theoretical:.2f} nm (n={closest_n2} to n={n1})")

# Example usage
compare_wavelengths(EXPERIMENTALwAVELENGTHoBTINAED, n1=3, n_max=21)  # n1=3 corresponds to Na-S lines

