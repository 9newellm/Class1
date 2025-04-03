import pandas as pd
import numpy as np

# Function to simulate the data
def generate_raman_data(file_name):
    # Example data for a Raman spectrometer test
    num_samples = 10  # Number of samples in the test

    # Simulate the Raman peaks for different samples
    wavelengths = np.linspace(520, 630, num_samples)  # Wavelengths from 520 to 630 nm
    intensities = np.random.normal(loc=500, scale=50, size=num_samples)  # Simulate intensities with noise
    peaks = np.array([520.7 + np.random.normal(loc=0, scale=0.2) for _ in range(num_samples)])  # Simulate peak positions around 520.7 nm
    resolutions = np.random.normal(loc=0.5, scale=0.05, size=num_samples)  # Simulate spectral resolution around 0.5 nm
    quantum_defects = np.random.normal(loc=0.001, scale=0.0001, size=num_samples)  # Simulate quantum defect values

    # Create a DataFrame
    data = pd.DataFrame({
        'Sample Number': np.arange(1, num_samples + 1),
        'Wavelength (nm)': wavelengths,
        'Intensity': intensities,
        'Raman Peak (nm)': peaks,
        'Resolution (FWHM, nm)': resolutions,
        'Quantum Defect': quantum_defects
    })

    headers = [
        "Trial Number", "Iteration Number", "Wavelength (nm)", 
        "Intensity", "Peak Wavelength (nm)", "Peak Intensity",
        "SNR", "MTF Value", "Notes"
    ]
    # Save to Excel
    data.to_excel(file_name, index=False)

# Generate the Raman data and save to Excel
generate_raman_data("raman_spectrometer_data.xlsx")
