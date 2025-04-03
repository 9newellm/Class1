import pandas as pd
import matplotlib.pyplot as plt

# Load the Raman data from an Excel file
def load_test_data(file_path):
    return pd.read_excel(file_path)

# Function to calculate quantum defects based on the measured peak wavelengths
def calculate_quantum_defects(data, theoretical_wavelengths=[589.5924, 589.1884]):
    measured_wavelengths = data['Wavelength (nm)']
    quantum_defects = []
    for measured_wavelength in measured_wavelengths:
        defect_1 = measured_wavelength - theoretical_wavelengths[0]  # D1 line
        defect_2 = measured_wavelength - theoretical_wavelengths[1]  # D2 line
        quantum_defects.append((defect_1, defect_2))
    return quantum_defects

# Function to create the LaTeX lab report
def create_lab_report_latex(data_file, report_file):
    doc_content = []

    # Add Title
    doc_content.append(r"\documentclass{article}")
    doc_content.append(r"\usepackage{graphicx}")
    doc_content.append(r"\usepackage{amsmath}")
    doc_content.append(r"\usepackage{longtable}")
    doc_content.append(r"\title{Raman Spectrometer Lab Report}")
    doc_content.append(r"\author{Your Name}")
    doc_content.append(r"\date{\today}")
    doc_content.append(r"\begin{document}")
    doc_content.append(r"\maketitle")

    # Add Abstract
    doc_content.append(r"\section*{Abstract}")
    doc_content.append(
        "This lab report documents the evaluation of a Raman spectrometer's performance, "
        "specifically using a 527 nm excitation laser, with a focus on spectral accuracy, resolution, and efficiency. "
        "The report further includes the calculation of quantum defects by comparing the measured wavelengths of atomic "
        "spectral lines (such as sodium D1 and D2) with their theoretical counterparts. The analysis aims to identify "
        "quantum defects and assess the spectrometer's precision in detecting atomic transitions."
    )

    # Add Test Procedure Section
    doc_content.append(r"\section*{Test Procedure}")
    doc_content.append(
        "The objective of this test is to evaluate the performance of a Raman spectrometer using a 527 nm excitation laser, "
        "including spectral accuracy, resolution, and efficiency. Additionally, the test procedure incorporates the calculation "
        "of quantum defects in atomic systems (e.g., sodium), by comparing the measured wavelengths of atomic spectral lines "
        "(e.g., sodium D1 and D2) with theoretical values. The procedure includes the following steps:"
    )
    doc_content.append(r"\begin{itemize}")
    doc_content.append(r"\item Environmental Conditions: Ensure the test is conducted under controlled temperature, humidity, and pressure conditions.")
    doc_content.append(r"\item Instrument Calibration: Calibration is verified using a silicon wafer as a reference sample.")
    doc_content.append(r"\item Alignment Checks: Ensure proper positioning of collimating and focusing mirrors.")
    doc_content.append(r"\item Atomic Line References: Sodium D-lines (589.5924 nm and 589.1884 nm) will be used as reference points.")
    doc_content.append(r"\item Data Collection: Measure the Raman spectra using the 527 nm excitation laser, and record the wavelengths of the sodium D-lines.")
    doc_content.append(r"\end{itemize}")



# Add Theory Section
    doc_content.append(r"\section*{Theory}")
    doc_content.append(
    "The primary goal of this experiment is to evaluate the performance of a Raman spectrometer in detecting the sodium D1 and D2 spectral lines "
    "and to calculate the quantum defects based on the measured wavelengths. This section provides the theoretical background for the experiment, "
    "which involves understanding the quantum defects and the principle behind the Czerny-Turner type spectrometer.\n\n"
    
    r"\textbf{Quantum Defects:}" + "\n"
    "Quantum defects refer to the deviations in the energy levels of an atom or ion. In the context of spectroscopy, these defects represent the difference "
    "between the observed (measured) wavelengths and the theoretical (predicted) wavelengths. These defects can be used to evaluate the performance and precision "
    "of a spectrometer. The quantum defect is calculated by comparing the measured spectral lines to the known theoretical wavelengths of atomic transitions.\n\n"
    
    r"In this experiment, the sodium D1 and D2 lines are used as reference points to calculate the quantum defects. The wavelengths of these lines are well known "
    "in atomic physics:\n"
    "- \textbf{D1 Line}: 589.5924 nm (transition from the 3P1/2 state to the 3S1/2 state)\n"
    "- \textbf{D2 Line}: 589.1884 nm (transition from the 3P3/2 state to the 3S1/2 state)\n\n"
    
    r"To calculate the quantum defects, we subtract the theoretical wavelengths of the D1 and D2 lines from the measured wavelengths, resulting in the quantum defect "
    "for each line:\n"
    "- Quantum Defect for D1 = Measured Wavelength (nm) - 589.5924 nm\n"
    "- Quantum Defect for D2 = Measured Wavelength (nm) - 589.1884 nm\n\n"
    
    r"\textbf{Czerny-Turner Type Spectrometer:}" + "\n"
    "The spectrometer used in this experiment is a \textbf{Czerny-Turner type spectrometer}, a widely used design in high-resolution spectroscopic measurements. It works based on the following principles:\n"
    "- \textbf{Collimation}: The light source is collimated (made parallel) using mirrors. This ensures the light entering the spectrometer is parallel.\n"
    "- \textbf{Dispersion}: The collimated light passes through a diffraction grating, which disperses the light into its constituent wavelengths. The grating works by diffracting light at different angles based on wavelength.\n"
    "- \textbf{Detection}: After the light is dispersed, it is focused onto a detector (typically a CCD or photodiode array), which records the intensity of light at each wavelength.\n"
    "- \textbf{Resolution}: The resolution of the spectrometer determines how finely it can distinguish between two close wavelengths. High resolution is important for precise measurements, especially for closely spaced lines like sodium D1 and D2.\n\n"
    
    "The sodium D-lines (589.5924 nm and 589.1884 nm) serve as reference points in this experiment. The quantum defects are calculated by comparing the measured wavelengths to these theoretical values.\n\n"
    
    r"\textbf{Raman Shift and Raman Peak:}" + "\n"
    "The Raman shift corresponds to the change in energy between the incident light and the scattered light, often represented as a shift in wavelength. "
    "The Raman Peak is observed at a specific wavelength where the scattering occurs, shifted from the excitation wavelength.\n\n"
    
    "Raman Shift (cm$^{-1}$) is calculated as follows:\n"
    r"\begin{equation*}"
    r"\Delta \tilde{\nu} = \frac{1}{\lambda_{\text{incident}}} - \frac{1}{\lambda_{\text{scattered}}}"
    r"\end{equation*}"
    r"Where: "
    r"\begin{itemize}"
    r"\item $\Delta \tilde{\nu}$ = Raman shift in cm$^{-1}$"
    r"\item $\lambda_{\text{incident}}$ = Wavelength of incident light (in nm)"
    r"\item $\lambda_{\text{scattered}}$ = Wavelength of scattered light (in nm)"
    r"\end{itemize}\n\n"
    
    r"\textbf{Resolution (FWHM):}" + "\n"
    "The resolution of the spectrometer is defined by the Full Width at Half Maximum (FWHM) of a spectral peak. It determines how well the spectrometer can distinguish two closely spaced spectral lines.\n\n"
    
    r"Resolution (FWHM) can be calculated from the spectral peak shape:\n"
    r"\begin{equation*}"
    r"FWHM = \text{width of the peak at half its maximum intensity}"
    r"\end{equation*}\n\n"
    
    r"\textbf{Quantum Defect Calculation:}" + "\n"
    "Quantum defects are calculated for the sodium D1 and D2 lines as follows:\n"
    r"\begin{equation*}"
    r"Defect_1 = \lambda_{\text{measured}} - 589.5924 \, \text{nm}"
    r"\end{equation*}"
    r"for D1 line and"
    r"\begin{equation*}"
    r"Defect_2 = \lambda_{\text{measured}} - 589.1884 \, \text{nm}"
    r"\end{equation*}"
    r"for D2 line.\n\n"
    
    "The quantum defect for each line represents the deviation of the measured wavelength from the known theoretical wavelength.\n"
    "Smaller defects indicate more accurate measurements by the spectrometer."
    )

    # # Add Theory Section
    # doc_content.append(r"\section*{Theory}")
    # doc_content.append(
    #     "The primary goal of this experiment is to evaluate the performance of a Raman spectrometer in detecting the sodium D1 and D2 spectral lines "
    #     "and to calculate the quantum defects based on the measured wavelengths. This section provides the theoretical background for the experiment, "
    #     "which involves understanding the quantum defects and the principle behind the Czerny-Turner type spectrometer.\n\n"
        
    #     r"\textbf{Quantum Defects:}" + "\n"
    #     "Quantum defects refer to the deviations in the energy levels of an atom or ion. In the context of spectroscopy, these defects represent the difference "
    #     "between the observed (measured) wavelengths and the theoretical (predicted) wavelengths. These defects can be used to evaluate the performance and precision "
    #     "of a spectrometer. The quantum defect is calculated by comparing the measured spectral lines to the known theoretical wavelengths of atomic transitions.\n\n"
        
    #     r"In this experiment, the sodium D1 and D2 lines are used as reference points to calculate the quantum defects. The wavelengths of these lines are well known "
    #     "in atomic physics:\n"
    #     "- \textbf{D1 Line}: 589.5924 nm (transition from the 3P1/2 state to the 3S1/2 state)\n"
    #     "- \textbf{D2 Line}: 589.1884 nm (transition from the 3P3/2 state to the 3S1/2 state)\n\n"
        
    #     r"To calculate the quantum defects, we subtract the theoretical wavelengths of the D1 and D2 lines from the measured wavelengths, resulting in the quantum defect "
    #     "for each line:\n"
    #     "- Quantum Defect for D1 = Measured Wavelength (nm) - 589.5924 nm\n"
    #     "- Quantum Defect for D2 = Measured Wavelength (nm) - 589.1884 nm\n\n"
        
    #     r"\textbf{Czerny-Turner Type Spectrometer:}" + "\n"
    #     "The spectrometer used in this experiment is a \textbf{Czerny-Turner type spectrometer}, a widely used design in high-resolution spectroscopic measurements. It works based on the following principles:\n"
    #     "- \textbf{Collimation}: The light source is collimated (made parallel) using mirrors. This ensures the light entering the spectrometer is parallel.\n"
    #     "- \textbf{Dispersion}: The collimated light passes through a diffraction grating, which disperses the light into its constituent wavelengths. The grating works by diffracting light at different angles based on wavelength.\n"
    #     "- \textbf{Detection}: After the light is dispersed, it is focused onto a detector (typically a CCD or photodiode array), which records the intensity of light at each wavelength.\n"
    #     "- \textbf{Resolution}: The resolution of the spectrometer determines how finely it can distinguish between two close wavelengths. High resolution is important for precise measurements, especially for closely spaced lines like sodium D1 and D2.\n\n"
        
    #     "The sodium D-lines (589.5924 nm and 589.1884 nm) serve as reference points in this experiment. The quantum defects are calculated by comparing the measured wavelengths to these theoretical values."
    # )

    # Add Test Data Table
    doc_content.append(r"\section*{Test Data}")
    doc_content.append("The following data was collected during the test:")

    # Load the data
    data = load_test_data(data_file)
    doc_content.append(r"\begin{longtable}{|c|c|c|c|c|c|}")
    doc_content.append(r"\hline")
    doc_content.append(r"Sample Number & Wavelength (nm) & Intensity & Raman Peak (nm) & Resolution (FWHM, nm) & Quantum Defect \\ \hline")
    doc_content.append(r"\endfirsthead")
    doc_content.append(r"\hline")
    doc_content.append(r"Sample Number & Wavelength (nm) & Intensity & Raman Peak (nm) & Resolution (FWHM, nm) & Quantum Defect \\ \hline")
    doc_content.append(r"\endhead")
    doc_content.append(r"\hline")
    for index, row in data.iterrows():
        doc_content.append(
            f"{row['Sample Number']} & {row['Wavelength (nm)']:.4f} & {row['Intensity']:.4f} & "
            f"{row['Raman Peak (nm)']:.4f} & {row['Resolution (FWHM, nm)']:.4f} & {row['Quantum Defect']:.4f} \\\\" 
        )
    doc_content.append(r"\hline")
    doc_content.append(r"\end{longtable}")

    # Add Equations Section
    doc_content.append(r"\section*{Equations}")
    doc_content.append(
        r"Quantum Defect Calculation:"
        r"\begin{equation*}"
        r"\Delta E = E_n - E_{n+1}"
        r"\end{equation*}"
        r"Where:"
        r"\begin{itemize}"
        r"\item $\Delta E$ = Quantum Defect"
        r"\item $E_n$ = Raman Peak of the n-th sample"
        r"\item $E_{n+1}$ = Raman Peak of the (n+1)-th sample"
        r"\end{itemize}"
    )

    # Add Results from Quantum Defect Calculation
    doc_content.append(r"\section*{Quantum Defect Analysis}")
    
    # Calculate quantum defects
    quantum_defects = calculate_quantum_defects(data)
    
    doc_content.append(r"The quantum defects are calculated by comparing the measured peak wavelengths "
        "to the theoretical wavelengths of sodium D1 and D2 lines. The quantum defect is "
        "the difference between the measured wavelength and the theoretical wavelength for each sodium line. "
        "The quantum defects for each measured peak are calculated as follows:")
    
    doc_content.append(r"For each peak:")
    doc_content.append(r"\begin{itemize}")
    doc_content.append(r"\item D1 Defect = Measured Wavelength - 589.5924 nm")
    doc_content.append(r"\item D2 Defect = Measured Wavelength - 589.1884 nm")
    doc_content.append(r"\end{itemize}")

    doc_content.append("The calculated quantum defects for each peak are as follows:")
    for i, (defect_1, defect_2) in enumerate(quantum_defects):
        doc_content.append(f"Peak {i + 1}: D1 Defect = {defect_1:.4f} nm, D2 Defect = {defect_2:.4f} nm")

        # Add Quantum Defects to a Table in the LaTeX Report
    doc_content.append(r"\section*{Quantum Defects Analysis}")
    doc_content.append("The calculated quantum defects for each peak are as follows:")

    # Create LaTeX table for quantum defects
    doc_content.append(r"\begin{longtable}{|c|c|c|}")
    doc_content.append(r"\hline")
    doc_content.append(r"Peak Number & D1 Defect (nm) & D2 Defect (nm) \\ \hline")
    doc_content.append(r"\endfirsthead")
    doc_content.append(r"\hline")
    doc_content.append(r"Peak Number & D1 Defect (nm) & D2 Defect (nm) \\ \hline")
    doc_content.append(r"\endAhead")
    doc_content.append(r"\hline")

    # Append each quantum defect for each peak
    for i, (defect_1, defect_2) in enumerate(quantum_defects):
        doc_content.append(f"{i + 1} & {defect_1:.4f} & {defect_2:.4f} \\\\")

    doc_content.append(r"\hline")
    doc_content.append(r"\end{longtable}")
    doc_content.append(r"\end{document}")

    # Save the document as a LaTeX file
    with open(report_file, 'w') as f:
        f.write("\n".join(doc_content))

    print(f"Lab report saved as {report_file}")


# Run the script
if __name__ == "__main__":
    data_file = "raman_spectrometer_data.xlsx"  # This file is generated by the previous script
    report_file = "Raman_Spectrometer_Lab_Report_with_Theory.tex"
    create_lab_report_latex(data_file, report_file)
