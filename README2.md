# Raman Spectrometer Quantum Defect Analysis

This project consists of several Python scripts that simulate Raman spectrometer data, analyze the data, and generate a detailed NASA-style test report with the results. The steps are as follows:

1. **Generate Raman Spectrometer Data**: Simulate data from a Raman spectrometer test, including Raman peaks, intensities, and quantum defects.
2. **Analyze the Data**: Process the data and calculate quantum defects based on the Raman peak positions.
3. **Generate a Test Report**: Create a NASA-style test report with the analysis results.

## Project Structure

/your-project-directory
│
├── raman_spectrometer_analysis
│   ├── raman_spectrometer_data_generation.py       # Script to generate the Raman data
│   ├── raman_data_analysis.py                     # Script to analyze the Raman data
│   ├── raman_test_report_generation.py            # Script to create the test report
│   ├── requirements.txt                           # Dependencies file
│   ├── main.py                                    # Main script to run all tasks
│   └── raman_analysis_results.xlsx                # Output file with analyzed results
│
└── README.md                                      # Project documentation

### Scripts Overview

1. **`raman_spectrometer_data_generation.py`**:

   - This script generates simulated Raman spectrometer data and saves it to an Excel file (`raman_spectrometer_data.xlsx`).
   - The data includes sample numbers, wavelengths, Raman peak positions, intensities, and quantum defect values.
2. **`raman_data_analysis.py`**:

   - This script processes the generated Raman data and calculates quantum defects using the formula `(Raman Peak (nm) - 520.7) / 1000` for each sample.
   - The results are saved to a new Excel file (`raman_analysis_results.xlsx`).
3. **`raman_test_report_generation.py`**:

   - This script takes the analysis results from the Excel file and generates a NASA-style test report in Word format (`Raman_Spectrometer_Test_Report.docx`).
   - The report includes the test objectives, conditions, and the analyzed data presented in a table format.

### Installation Instructions

1. **Install Python**: Ensure Python 3.6 or higher is installed on your system.
2. **Install Required Dependencies**:
   You will need the following Python packages:

   - `pandas`
   - `numpy`
   - `python-docx`
   - `openpyxl`

   You can install them using `pip`:

   ```bash
   pip install -r requirements.txt
   ```
