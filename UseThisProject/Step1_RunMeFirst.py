import os
import subprocess


""" Creates visual studio enviornment with same extensions as my computer."""


# Define paths
project_directory = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
setup_folder = os.path.join(project_directory, "VisualStudioSetup")
extensions_file = os.path.join(setup_folder, "extensions.txt")
visual_studio_script = os.path.join(setup_folder, "VisualStudio.py")

# Ensure VisualStudioSetup exists
if not os.path.exists(setup_folder):
    os.makedirs(setup_folder)
    print(f"📁 Created missing directory: {setup_folder}")

# Ensure extensions.txt exists
if not os.path.exists(extensions_file):
    with open(extensions_file, "w") as f:
        f.write("")  # Create an empty file
    print(f"📄 Created missing file: {extensions_file}")

# Ensure VisualStudio.py exists before execution
if os.path.exists(visual_studio_script):
    print(f"🚀 Executing {visual_studio_script}...")
    subprocess.run(["python", visual_studio_script], check=True)
else:
    print(f"❌ Error: {visual_studio_script} not found. Please ensure it's in the correct directory.")
