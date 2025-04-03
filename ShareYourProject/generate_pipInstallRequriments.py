import subprocess
import os

""" This file must be in the main project folder to run so just copy and paste it there and then run it. """

def generate_pip_requirements():
    try:
        # Run pip freeze to get the list of installed packages
        result = subprocess.run(["pip", "freeze"], capture_output=True, text=True, check=True)
        
        # Get the output from pip freeze (installed packages list)
        installed_packages = result.stdout        
        
        # Define the path for requirements.txt
        requirements_file_path = "./VisualStudioSetup/requirements.txt"
        
        # Write the installed packages to the requirements.txt file
        with open(requirements_file_path, "w") as f:
            f.write(installed_packages)
        
        print(f"✅ requirements.txt has been generated successfully at {requirements_file_path}")
    
    except subprocess.CalledProcessError as e:
        print(f"❌ Error occurred while running pip freeze: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function to generate the pip install file
if __name__ == "__main__":
    generate_pip_requirements()
