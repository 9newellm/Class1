# main.py
import subprocess

def run_scripts():
    print("Running Raman Spectrometer Data Generation...")
    subprocess.run(["python", "generate_raman_data.py"], check=True)

    print("Running Raman Data Analysis...")
    subprocess.run(["python", "analyze_raman_data_Q_Defects.py"], check=True)

    print("Generating Raman Test Report...")
    subprocess.run(["python", "Q_Defects_TestReport.py"], check=True)

    print("Workflow complete! The data has been processed and the repalort is generated.")

if __name__ == "__main__":
    run_scripts()
