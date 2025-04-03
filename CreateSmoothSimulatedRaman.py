import openpyxl
import random
import numpy as np

def create_smooth_raman_data(file_name):
    # Create a new workbook and activate it
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Raman Test Data"

    # Add headers for your data collection
    headers = [
        "Trial Number", "Iteration Number", "Wavelength (nm)", 
        "Intensity", "Peak Wavelength (nm)", "Peak Intensity",
        "SNR", "MTF Value", "Notes"
    ]
    ws.append(headers)

    # Generate fake data for 5 trials, each with 3 iterations
    for trial in range(1, 6):  # 5 trials
        for iteration in range(1, 4):  # 3 iterations per trial
            # Simulate a range of wavelengths (e.g., 530 to 630 nm)
            wavelength = np.linspace(530, 630, 100)  # 100 wavelength points between 530 and 630 nm
            
            # Generate smooth intensity values (simulate Raman peaks using a Gaussian-like function)
            intensity = 1500 + 200 * np.sin(np.pi * (wavelength - 530) / 100) + 100 * np.random.randn(len(wavelength))  # Add noise to the sinusoidal curve

            # Add some random peak shifts and intensity variations
            peak_wavelength = wavelength[np.argmax(intensity)]  # Peak wavelength is where intensity is maximum
            peak_intensity = np.max(intensity)  # Peak intensity is the maximum value in the simulated intensity curve

            # Simulate SNR and MTF values
            snr = random.uniform(30, 50)  # SNR between 30 and 50
            mtf = random.uniform(0.8, 1.0)  # MTF value between 0.8 and 1.0

            # Add the simulated data to the worksheet for each trial/iteration
            for i in range(len(wavelength)):
                ws.append([
                    trial, iteration, wavelength[i], intensity[i], peak_wavelength, 
                    peak_intensity, round(snr, 2), round(mtf, 2), "Simulated data"
                ])

    # Save the workbook
    wb.save(file_name)

# Create the smooth fake Excel file template
create_smooth_raman_data('smooth_simulated_raman_test_data.xlsx')
