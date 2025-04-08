import subprocess
import os

""" Creates python enviornment with same packages as my computer."""

def install_requirements():
    try:
        # Define the path to the requirements.txt file
        requirements_path = os.path.join("VisualStudioSetup", "requirements.txt")
        
        # Check if the requirements.txt file exists
        if not os.path.exists(requirements_path):
            print(f"❌ Error: {requirements_path} does not exist. Please ensure the file is present.")
            return
        
        # Run pip install using the requirements.txt file
        print(f"📦 Installing packages from {requirements_path}...")
        subprocess.run(["pip", "install", "-r", requirements_path], check=True)
        
        print("✅ All packages have been successfully installed.")
    
    except subprocess.CalledProcessError as e:
        print(f"❌ Error occurred while installing the packages: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function to install the packages
if __name__ == "__main__":
    install_requirements()
