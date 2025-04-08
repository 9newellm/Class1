import os
import sys
import zipfile
import ctypes
import platform
import subprocess
import clr  # Import pythonnet for .NET interaction

# Get the current script's directory (this helps ensure paths are relative to the script's location)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the zip file and the extraction directory
zip_file_path = os.path.join(script_dir, 'ASCOM-Python-Programming.zip')  # Path to the zip file
extract_dir = os.path.join(script_dir, 'ASCOM-Python-Programming')  # Folder where you want to unzip the DLLs

# Check if the zip file exists
if not os.path.exists(zip_file_path):
    print(f"Error: Zip file {zip_file_path} does not exist.")
    sys.exit(1)

# Extract the ZIP file if the directory doesn't already exist
if not os.path.exists(extract_dir):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)  # Extract the contents to the target folder
        print(f"Successfully extracted zip file to {extract_dir}")
    except Exception as e:
        print(f"Error extracting the zip file: {e}")
        sys.exit(1)

# Now, set the path to the extracted DLL folder
dll_folder = extract_dir  # Now use the extracted folder as the DLL folder

# Ensure that all necessary DLLs are available in the folder
dll_files = [
    'FLISharp.dll',
    'log4net.dll',
    'System.ValueTuple.dll',
    'libflipro.x64.dll',
    'libflipro.x86.dll'
]

# Function to register a DLL using regsvr32
def register_dll(dll_path):
    try:
        # Run regsvr32 command to register the DLL
        result = subprocess.run(
            ['regsvr32', '/s', dll_path],  # /s means silent mode, no user interaction
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"Successfully registered {dll_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to register {dll_path}. Error: {e.stderr.decode('utf-8')}")

# Check if all DLLs exist in the extracted folder and register them
for dll in dll_files:
    dll_path = os.path.join(dll_folder, dll)
    print(dll_path)
    print("===================")

    if not os.path.exists(dll_path):
        print(f"Error: Missing DLL file {dll} at {dll_path}")
        sys.exit(1)  # Exit the script if any required DLL is missing
    else:
        print(f"Registering {dll_path}...")
        register_dll(dll_path)

# Check Python architecture (32-bit or 64-bit)
python_arch = platform.architecture()[0]
print(f"Python architecture: {python_arch}")

# Load .NET Assemblies (FliSharp, log4net, etc.) with pythonnet
try:
    clr.AddReference(os.path.join(dll_folder, 'FliSharp.dll'))
    clr.AddReference(os.path.join(dll_folder, 'log4net.dll'))
    clr.AddReference(os.path.join(dll_folder, 'System.ValueTuple.dll'))
    print("Successfully loaded .NET assemblies (FliSharp, log4net, System.ValueTuple).")
except Exception as e:
    print(f"Error loading .NET assemblies: {e}")
    sys.exit(1)

# Load Native DLLs (libflipro.x64.dll, libflipro.x86.dll) with ctypes
try:
    # Load the appropriate native DLL based on Python architecture
    if python_arch == '64bit':
        lib_fli = ctypes.CDLL(os.path.join(dll_folder, 'libflipro.x64.dll'))
        print("Successfully loaded libflipro.x64.dll")
    elif python_arch == '32bit':
        lib_fli = ctypes.CDLL(os.path.join(dll_folder, 'libflipro.x86.dll'))
        print("Successfully loaded libflipro.x86.dll")
    else:
        print("Error: Unsupported Python architecture.")
        sys.exit(1)
except Exception as e:
    print(f"Error loading native DLLs: {e}")
    sys.exit(1)  # Exit the script if there is an issue with loading native DLLs

# Example Camera connection function using the FliSharp library
def connect_camera():
    try:
        # Call .NET methods to connect to the camera using FliSharp
        # Example: camera = Camera()  # Replace with actual class and methods
        print("Connected to the camera")
        return "Camera Object"  # Replace with actual object return
    except Exception as e:
        print(f"Error connecting to the camera: {e}")
        sys.exit(1)  # Exit if connection fails

def main():
    print("Starting camera connection script...")
    
    # Connect to the camera
    cam = connect_camera()
    
    # Optionally, you can add additional code to interact with the camera, take images, or capture data
    print("Camera interaction complete.")
    
    # Close the camera when done
    try:
        # Example: cam.Close()  # Replace with actual close method if available
        print("Camera connection closed.")
    except Exception as e:
        print(f"Error closing camera: {e}")

# Run the script
if __name__ == "__main__":

    """ This script will run to install all the drivers, DLLs properly, and register them. """
    main()
 