import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

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

# Function to calculate FWHM of the peaks
def generate_fwhm_plot(df, output_image_path):
    "df = data "
    # Step 1: Identify the peak's maximum intensity
    peak_intensity = df['Intensity'].max()
# ['Intensity'], data['Wavelength (nm)']
    # Step 2: Determine the half-maximum value
    half_max = peak_intensity / 2

    # Step 3: Find indices where intensity crosses the half-maximum value
    # First, find where intensity rises above half_max
    rising_indices = np.where(df['Intensity'] > half_max)[0]
    # Then, find where intensity falls below half_max
    falling_indices = np.where(df['Intensity'] < half_max)[0]

    # Ensure there are rising and falling indices
    if rising_indices.size > 0 and falling_indices.size > 0:
        # The first index where intensity rises above half_max
        x1 = df.iloc[rising_indices[0]]['Wavelength (nm)']
        # The last index where intensity falls below half_max
        x2 = df.iloc[falling_indices[-1]]['Wavelength (nm)']
        # Calculate FWHM
        fwhm = x2 - x1
        print(f"The Full Width at Half Maximum (FWHM) is approximately {fwhm:.2f} nm")
    else:
        print("Half-maximum not found within the intensity range.")


    # Try to find the left and right points where intensity crosses half_max
    print("peak_intensity", peak_intensity)
    print("half_max", half_max)
    left_index = np.where(np.atleast_1d(peak_intensity) <= half_max)[0] # index the peak value
    right_index = np.where(np.atleast_1d(peak_intensity) <= half_max)[0]
    
    if len(left_index) == 0 or len(right_index) == 0:
        print("Half maximum not found within the intensity range.")
        return
    
    left_index = left_index[-1]  # The last index before the peak
    right_index = right_index[0] + np.where(intensity = np.atleast_1d(peak_intensity))  # The first index after the peak
    
    # Plot the intensity vs. wavelength
    plt.figure(figsize=(10, 6))
    intensity, wavelength = df['Intensity'], df['Wavelength (nm)']
    plt.plot(wavelength, intensity, label='Intensity')
    plt.plot([wavelength[left_index], wavelength[right_index]], [half_max, half_max], 'r--', label='Half Maximum')
    plt.plot([wavelength[left_index], wavelength[left_index]], [0, half_max], 'g--', label='Left Half-Maximum')
    plt.plot([wavelength[right_index], wavelength[right_index]], [0, half_max], 'b--', label='Right Half-Maximum')
    plt.scatter([wavelength[left_index], wavelength[right_index]], [half_max, half_max], color='black', zorder=5)
    
    plt.title('Full Width at Half Maximum (FWHM) Calculation')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.legend()
    plt.grid(True)
    
    # Save the plot as a PNG file
    plt.savefig(output_image_path, format='png')
    plt.close()

# Function to create the LaTeX lab report
def create_lab_report_latex(data_file, report_file):

    # Load the data
        
    # Generate the FWHM plot and save it as a .png image
    fwhm_plot_path = 'fwhm_plot.png' #################################################################### .png file for imaging description
    data = load_test_data(data_file) #### First Load of data. (Load later as weel #!)
    generate_fwhm_plot(data, fwhm_plot_path)
    
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
        
        
        r"The primary goal of this experiment is to evaluate the performance of a Raman spectrometer in detecting the sodium D1 and D2 spectral lines "
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
    
    r"Raman Shift (cm$^{-1}$) is calculated as follows:\n"
    r"\begin{equation*}"
    r"\Delta \tilde{\nu} = \frac{1}{\lambda_{\text{incident}}} - \frac{1}{\lambda_{\text{scattered}}}"
    r"\end{equation*} "
    r"Where: "
    r"\begin{itemize}"
    r"\item $\Delta \tilde{\nu}$ = Raman shift in cm$^{-1}$"
    r"\item $\lambda_{\text{incident}}$ = Wavelength of incident light (in nm)"
    r"\item $\lambda_{\text{scattered}}$ = Wavelength of scattered light (in nm)"
    r"\end{itemize}\n\n"
    
    r"\textbf{Resolution (FWHM):}" + "\n"
    r"The resolution of the spectrometer is defined by the Full Width at Half Maximum (FWHM) of a spectral peak. It determines how well the spectrometer can distinguish two closely spaced spectral lines.\n\n") 
    


    # Existing LaTeX document content...


    # Add image to the LaTeX report
    doc_content.append(r"\section*{FWHM Calculation and Intensity Plot}")
    doc_content.append(
        "The Full Width at Half Maximum (FWHM) for the primary Raman peak is calculated to determine the resolution of the spectrometer. "
        "Below is the plot showing the FWHM calculation with the half-maximum lines indicated."
    )
    doc_content.append(r"\begin{figure}[h!]")
    doc_content.append(r"\centering")
    doc_content.append(r"\includegraphics[width=0.7\textwidth]{" + fwhm_plot_path + r"}")
    doc_content.append(r"\caption{FWHM Calculation for the Raman Peak}")
    doc_content.append(r"\end{figure}")
    
    doc_content.append(    r"""
    \section*{Full Width at Half Maximum (FWHM) Calculation}

    The Full Width at Half Maximum (FWHM) is a widely used measure of the width of a spectral peak, which represents the resolution of the spectrometer. It is defined as the difference between the wavelengths at which the intensity falls to half of the peak value (half-maximum). FWHM gives an indication of how well the spectrometer can resolve closely spaced spectral features. 

    In this experiment, we calculate the FWHM of the main Raman peak to determine the resolution of the spectrometer.

    The following steps are involved in calculating FWHM for a spectral peak:

    \begin{enumerate}
        \item \textbf{Identify the peak:} First, we locate the peak in the intensity data. This is done by finding local maxima in the intensity using the \texttt{find\_peaks} function.
        \item \textbf{Half-Maximum Value:} The peak value is divided by 2 to obtain the half-maximum value. This value represents the intensity level at which the spectral peak width is measured.
        \item \textbf{Find the left and right points:} We locate the points on the left and right sides of the peak where the intensity falls to half of the maximum value. These points are determined by searching for the wavelength values at which the intensity crosses the half-maximum.
        \item \textbf{Calculate the FWHM:} The FWHM is computed by subtracting the wavelength at the left crossing from the wavelength at the right crossing.
    \end{enumerate}

    The FWHM is given by the formula:

    \[
    FWHM = \lambda_{\text{right}} - \lambda_{\text{left}}
    \]

    Where:
    \begin{itemize}
        \item $\lambda_{\text{right}}$ is the wavelength at which the intensity falls to half-maximum on the right side of the peak.
        \item $\lambda_{\text{left}}$ is the wavelength at which the intensity falls to half-maximum on the left side of the peak.
    \end{itemize}

    This process ensures that the width of the peak is accurately calculated, providing an assessment of the spectrometer's resolution.

    \section*{Assumptions}

    Several assumptions are made during the FWHM calculation:

    \begin{itemize}
        \item \textbf{Symmetry of the Peak:} The calculation assumes that the spectral peak is symmetric around its maximum. This is a common assumption in spectral analysis, though real spectra may exhibit asymmetry due to instrumental effects or sample characteristics. If the peak is asymmetric, the FWHM value might not fully represent the true width of the feature.
        \item \textbf{Single Peak Dominance:} The function assumes that the Raman spectrum contains a dominant peak, which is treated as the primary peak for FWHM calculation. If there are multiple overlapping peaks, this approach may not yield accurate results.
        \item \textbf{Sufficient Resolution of Data:} The intensity data and wavelength values must have sufficient resolution to accurately locate the half-maximum intensity points. If the spectral data is too coarse, the FWHM calculation may be inaccurate.
        \item \textbf{Constant Intensity Threshold:} The half-maximum value is computed as half of the peak intensity value, assuming this constant threshold. This works well for most ideal Gaussian-shaped peaks but may require adjustment for other shapes.
        \item \textbf{No Background Subtraction:} The intensity data is assumed to be free of significant background noise or contributions that would shift the baseline. In real experimental data, background subtraction may be necessary before calculating the FWHM.
    \end{itemize}

    Below is the implementation of the FWHM calculation:

    \begin{verbatim}
    def calculate_fwhm(intensity, wavelength):
        # Find peaks in the intensity data
        peaks, _ = find_peaks(intensity, height=0)
        
        # Assume the first peak is the primary Raman peak
        peak_index = peaks[0]
        peak_value = intensity[peak_index]
        
        # Half Maximum Value
        half_max = peak_value / 2
        
        # Find the left and right points where intensity crosses half_max
        left_index = np.where(intensity[:peak_index] <= half_max)[0][-1]
        right_index = np.where(intensity[peak_index:] <= half_max)[0][0] + peak_index
        
        # Calculate FWHM
        fwhm = wavelength[right_index] - wavelength[left_index]
        return fwhm
    \end{verbatim}
    """)

    doc_content.append( 
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
    data_file = "raman_spectrometer_data_with_sample.xlsx"  # This file is generated by the previous script
    report_file = "Raman_Spectrometer_Lab_Report_with_Theory.tex"
    create_lab_report_latex(data_file, report_file)

