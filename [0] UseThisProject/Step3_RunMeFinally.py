import os
import subprocess
from datetime import datetime

# Define paths
project_directory = os.path.dirname(os.path.abspath(__file__))  # Get script's directory
results_folder = os.path.join(project_directory, "Run_Me_Results_File")
simulation_script = os.path.join(project_directory, "CreateSmoothSimulatedRaman.py")
analysis_script = os.path.join(project_directory, "AnalyzeRamanSpectra.py")

# Ensure results folder exists
if not os.path.exists(results_folder):
    os.makedirs(results_folder)
    print(f"📁 Created results directory: {results_folder}")

# Define output file path
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(results_folder, f"run_output_{timestamp}.txt")

# Function to capture output of a subprocess
def run_and_capture(script_path):
    try:
        # Run the script and capture the output
        result = subprocess.run(["python", script_path], capture_output=True, text=True, check=True)
        return result.stdout  # Return only the standard output (stdout)
    except subprocess.CalledProcessError as e:
        return f"❌ Error occurred while running {script_path}: {e}\n{e.output}"

# Open the output file to write
with open(output_file, "w") as output:
    # Run CreateSmoothSimulatedRaman.py and capture its output
    if os.path.exists(simulation_script):
        print(f"🚀 Running {simulation_script}...")
        simulation_output = run_and_capture(simulation_script)
        output.write(f"===== Simulation Script Output =====\n{simulation_output}\n\n")
    else:
        output.write(f"❌ Error: {simulation_script} not found!\n\n")
    
    # Run AnalyzeRamanSpectra.py and capture its output
    if os.path.exists(analysis_script):
        print(f"🔎 Running {analysis_script}...")
        analysis_output = run_and_capture(analysis_script)
        output.write(f"===== Analysis Script Output =====\n{analysis_output}\n\n")
    else:
        output.write(f"❌ Error: {analysis_script} not found!\n\n")

print(f"✅ All processes completed. Output saved in '{output_file}'.")
