import pandas as pd
import numpy as np
import random

# Function to simulate the data
def generate_raman_data(file_name):
    # Increased number of samples for more comprehensive data
    num_samples = 1000  # Number of samples in the test

    # Simulate the Raman peaks for different samples
    wavelengths = np.linspace(520, 630, num_samples)  # Wavelengths from 520 to 630 nm
    intensities = np.random.normal(loc=500, scale=50, size=num_samples)  # Simulate intensities with noise
    peaks = 520.7 + np.random.normal(loc=0, scale=0.2, size=num_samples)  # Simulate peak positions around 520.7 nm
    resolutions = np.random.normal(loc=0.5, scale=0.05, size=num_samples)  # Simulate spectral resolution around 0.5 nm
    quantum_defects = np.random.normal(loc=0.001, scale=0.0001, size=num_samples)  # Simulate quantum defect values
    from scipy.signal import savgol_filter

    # Apply Savitzky-Golay filter
    intensities = savgol_filter(intensities, window_length=51, polyorder=3)

    # Additional simulated data
    trial_numbers = np.random.randint(1, 6, size=num_samples)  # Trial numbers between 1 and 5
    iteration_numbers = np.random.randint(1, 4, size=num_samples)  # Iteration numbers between 1 and 3
    peak_intensities = np.random.normal(loc=1500, scale=200, size=num_samples)  # Simulated peak intensities
    snr_values = np.random.uniform(30, 50, size=num_samples)  # SNR values between 30 and 50
    mtf_values = np.random.uniform(0.8, 1.0, size=num_samples)  # MTF values between 0.8 and 1.0
    notes = ['Simulated data' for _ in range(num_samples)]  # Notes for each sample

    # Create a DataFrame
    data = pd.DataFrame({
        'Sample Number': np.arange(1, num_samples + 1),
        'Trial Number': trial_numbers,
        'Iteration Number': iteration_numbers,
        'Wavelength (nm)': wavelengths,
        'Intensity': intensities,
        'Raman Peak (nm)': peaks,
        'Resolution (FWHM, nm)': resolutions,
        'Quantum Defect': quantum_defects,
        'Peak Intensity': peak_intensities,
        'SNR': snr_values,
        'MTF Value': mtf_values,
        'Notes': notes
    })

    # Save to Excel
    data.to_excel(file_name, index=False)

# Generate the Raman data and save to Excel
generate_raman_data("raman_spectrometer_data_with_sample.xlsx")


# All they did was overwhelm her. And so, she did bad anyway. 
# It only validated the argement that they are targeting her. 
# We have documneted a massive 