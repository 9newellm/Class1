import openpyxl
import random

def create_fake_raman_data(file_name):
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
            wavelength = random.randint(530, 630)
            
            # Simulate intensity values with some variation
            intensity = random.randint(1200, 1800) + random.random() * 200  # Random intensity around 1500

            # Simulate peak wavelength and intensity near the current wavelength
            peak_wavelength = wavelength + random.uniform(-2, 2)  # Peak wavelength with small fluctuation
            peak_intensity = intensity + random.uniform(-100, 100)  # Peak intensity with small fluctuation

            # Simulate SNR and MTF values
            snr = random.uniform(30, 50)  # SNR between 30 and 50
            mtf = random.uniform(0.8, 1.0)  # MTF value between 0.8 and 1.0

            # Add the simulated data to the worksheet
            ws.append([
                trial, iteration, wavelength, intensity, peak_wavelength, 
                peak_intensity, round(snr, 2), round(mtf, 2), "Simulated data"
            ])

    # Save the workbook
    wb.save(file_name)

# Create the fake Excel file template
create_fake_raman_data('simulated_raman_test_data.xlsx')
