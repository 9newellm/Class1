# Raman Spectra Data Analysis

## Project Name: Raman Spectra Data Analysis

### Description:

This Python script analyzes Raman spectra data by identifying peaks and visualizing the results. It accepts Raman data in CSV format and processes the data to detect significant peaks, then generates a plot of the spectra with the identified peaks. It also returns a DataFrame with information about the detected peaks, including wavelength and intensity.

### Requirements:

- Python 3.x
- Libraries: `pandas`, `numpy`, `matplotlib`, `scipy`, `openpyxl`
  - You can install the required libraries by running:
    ```bash
    pip install pandas numpy matplotlib scipy openpyxl
    ```

### Usage:

1. **Prepare Data:**

   - Your data file should be in CSV format and contain at least two columns:
     - `Wavelength (nm)`
     - `Intensity`
   - The CSV file should look something like this:
     ```csv
     Wavelength,Intensity
     530,1000
     531,1100
     532,1050
     ...
     ```
2. **Running the Script:**

   - Place the data file (e.g., `raman_spectra_data.csv`) in the same directory as the script.
   - Open the Python script (`raman_data_analysis.py`).
   - Ensure that the path to your data file is correctly specified in the script.
3. **Execute the Script:**

   - Run the script:
     ```bash
     python raman_data_analysis.py
     ```
   - The script will:
     - Load the data from the CSV file.
     - Find peaks in the Raman spectra.
     - Display a plot showing the spectra with the peaks identified.
     - Print a DataFrame containing the peak wavelengths and intensities.

### Output:

- The script will generate a plot of the Raman spectra, showing the detected peaks.
- It will also output a DataFrame containing the following information:
  - `Peak Wavelength (nm)`
  - `Peak Intensity`

### Example Output:

```plaintext
   Peak Wavelength (nm)   Peak Intensity
0                  541.5            1600
1                  550.0            1450
...
```
