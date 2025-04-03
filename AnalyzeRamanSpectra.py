import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl


""" This can be utlized to obtain the FWHM - full width half maximum. """

# Function to analyze Raman spectra data
def analyze_raman_data(file_path):
    # Load the Raman data from CSV or Excel file
    data = pd.read_excel(file_path)  # You can use pd.read_excel() if the data is in Excel
    
    # Assume columns are: 'Wavelength' and 'Intensity'
    wavelength = data['Wavelength (nm)']
    intensity = data['Intensity']
    
    # Find peaks in the Raman spectra (local maxima detection)
    peaks = []
    for i in range(1, len(intensity) - 1):
        if intensity[i] > intensity[i - 1] and intensity[i] > intensity[i + 1]:
            peaks.append(i)
    
    # Plot the Raman spectra
    plt.figure(figsize=(10,6))
    plt.plot(wavelength, intensity, label='Raman Spectra')
    plt.plot(wavelength[peaks], intensity[peaks], 'ro', label='Raman Peaks')
    plt.title('Raman Spectra with Identified Peaks')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.legend()
    plt.show()

    # Return peak information for analysis
    peak_wavelengths = wavelength[peaks]
    peak_intensities = intensity[peaks]
    
    return pd.DataFrame({
        'Peak Wavelength (nm)': peak_wavelengths,
        'Peak Intensity': peak_intensities
    })

from ProjectConfig import * 
# Example: Analyze data from a specific file
if ISTEST: 
    peaks = analyze_raman_data(ISNAME_FOR_TEST)
else: # not Test Data File
    peaks = analyze_raman_data('raman_spectra_data.csv')

print(peaks) # return peaks which we can use to calculate FWHm later. 


# need to figure out how obtain this data relates to the peak intensity 