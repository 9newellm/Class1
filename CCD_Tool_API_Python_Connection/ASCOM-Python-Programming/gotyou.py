import clr  # pythonnet
import os




import ctypes

# Load the DLL
dll_path = r'C:\Users\vehem\Downloads\Berhane\CCD_Tool_API_Python_Connection\ASCOM-Python-Programming\libflipro.x64.dll'
try:
    lib = ctypes.CDLL(dll_path)
    print(f"Successfully loaded the DLL: {dll_path}")
except OSError as e:
    print(f"Error loading DLL: {e}")

# List of function names you want to check
function_names = ['initialize_camera', 'start_capture', 'stop_capture']

# Check if functions exist
for function_name in function_names:
    try:
        func = getattr(lib, function_name)
        print(f"Function '{function_name}' exists in the DLL.")
    except AttributeError:
        print(f"Function '{function_name}' does not exist in the DLL.")

exit()


# test 2 
import ctypes

# Load the DLL (adjust the path as needed)
lib = ctypes.CDLL(r'C:\Users\vehem\Downloads\Berhane\CCD_Tool_API_Python_Connection\ASCOM-Python-Programming\libflipro.x64.dll') 

# Example: Assume the DLL has a function called 'initialize_camera'
# that takes no arguments and returns an integer.
initialize_camera = lib.initialize_camera
initialize_camera.restype = ctypes.c_int  # Specify the return type

try:
    initialize_camera = lib.initialize_camera
    initialize_camera.restype = ctypes.c_int  # Specify the return type
    result = initialize_camera()  # Call the function
    print(f"Camera initialized: {result}")
except AttributeError:
    print("Function not found in DLL.")


exit()

# test 1 -- any .dll can function 
import clr
clr.AddReference('System.Windows.Forms')
import System.Windows.Forms as WinForms

exit()


# Load the .NET assembly (DLL) into the Python environment
clr.AddReference(r'C:\Users\vehem\Downloads\Berhane\CCD_Tool_API_Python_Connection\ASCOM-Python-Programming\libflipro.x64.dll')

# Now, import the namespace and class from the assembly
# Replace 'Namespace' and 'FlipProcessorCameraManager' with the actual namespace and class names
from Namespace import FlipProcessorCameraManager

# Create an instance of the FlipProcessorCameraManager
camera_manager = FlipProcessorCameraManager()

# Initialize the camera or perform other setup steps
# Check if there's an Initialize() method or other methods for camera setup
camera_manager.Initialize()  # Example method (replace with the actual method)

# Now, you can call methods on the camera_manager object
result = camera_manager.SomeMethod()  # Replace with an actual method

# Output the result
print(result)


