# Import General pytohn improts
import win32com.client
from win32com.universal import com_error
import numpy as np
import matplotlib.pyplot as plt
import time

## Import General Configuration Tools 
from ASCOM_CONFIG_API import * 
import os 

import clr
script_dir = os.path.dirname(os.path.abspath(__file__))
clr.AddReference(script_dir+'/CCD_Tool_API_Python_Connection/ASCOM-Python-Programming/libflipro.x64.dll')

clr.AddReference(script_dir+'/CCD_Tool_API_Python_Connection/ASCOM-Python-Programming/libflipro.x86.dll')

def connect_camera():
    """
    Connects to the FLI Kepler camera using the ASCOM interface.

    Input:
        None

    Output:
        camera (win32com.client.Dispatch object): 
            A reference to the connected camera object, allowing interaction with the camera.
    """
    cam = win32com.client.Dispatch(ASCOM_FLI_KEPLER_CAMERA)
    if not cam.Connected:
        print('Connecting to the camera...')
        cam.Connected = True
    if not cam.Connected:
        print('Unable to connect to the camera')
        exit(-1)
    print('Connected to the camera!')
    return cam

def disconnect_camera(cam):
    """
    Disconnects from the FLI Kepler camera.

    Input:
        cam (win32com.client.Dispatch object): 
            The connected camera object that needs to be disconnected.

    Output:
        None
    """
    print('Disconnecting from the camera...')
    cam.Connected = False

def get_camera_properties(cam):
    """
    Retrieves and prints various properties of the connected camera.

    Input:
        cam (win32com.client.Dispatch object): 
            The connected camera object.

    Output:
        None
    """
    properties = {
        'Description': cam.Description,
        'DriverInfo': cam.DriverInfo,
        'DriverVersion': cam.DriverVersion,
        'InterfaceVersion': str(cam.InterfaceVersion),
        'Name': cam.Name,
        'CameraState': str(cam.CameraState),
        'PixelSizeX': str(cam.PixelSizeX),
        'PixelSizeY': str(cam.PixelSizeY),
        'CameraXSize': str(cam.CameraXSize),
        'CameraYSize': str(cam.CameraYSize),
        'NumX': str(cam.NumX),
        'NumY': str(cam.NumY),
        'StartX': str(cam.StartX),
        'StartY': str(cam.StartY),
        'BinX': str(cam.BinX),
        'BinY': str(cam.BinY),
        'MaxBinX': str(cam.MaxBinX),
        'MaxBinY': str(cam.MaxBinX),
        'CCDTemperature': str(cam.CCDTemperature),
        'HeatSinkTemperature': str(cam.HeatSinkTemperature),
        'CanAbortExposure': str(cam.CanAbortExposure),
        'CanAsymmetricBin': str(cam.CanAsymmetricBin),
        'CanGetCoolerPower': str(cam.CanGetCoolerPower),
        'CanPulseGuide': str(cam.CanPulseGuide),
        'CanSetCCDTemperature': str(cam.CanSetCCDTemperature),
        'CanStopExposure': str(cam.CanStopExposure),
        'CanFastReadout': str(cam.CanFastReadout),
        'CoolerOn': str(cam.CoolerOn),
        'CoolerPower': str(cam.CoolerPower),
        'HasShutter': str(cam.HasShutter),
        'ExposureMax': str(cam.ExposureMax),
        'ExposureMin': str(cam.ExposureMin),
    }
    
    for key, value in properties.items():
        print(f'{key}: {value}')

def get_camera_modes(cam):
    """
    Retrieves and prints a list of available camera modes.

    Input:
        cam (win32com.client.Dispatch object): 
            The connected camera object.

    Output:
        None
    """
    try:
        modes = cam.Action(ASCOM_FLI_KEPLER_GET_MODESLIST, '')
        print('Modes list: ')
        for i in range(modes.Count):
            print(f' #{i} -> {modes[i]}')
    except com_error as error:
        _, msg, exc, _ = error.args
        _, _, msg2, _, _, _ = exc
        print(f'Oops! {msg} {msg2}')

def set_camera_mode(cam, mode_index):
    """
    Sets the camera to a specified mode.

    Input:
        cam (win32com.client.Dispatch object): 
            The connected camera object.
        mode_index (int): 
            The index of the mode to set. Each mode corresponds to different camera settings (e.g., HDR mode).

    Output:
        None
    """
    try:
        cam.Action(ASCOM_FLI_KEPLER_SET_MODE, str(mode_index))
        print(f'Set Mode: res = {mode_index}')
    except com_error as error:
        print(f'Error setting mode: {error}')

def get_gain_tables(cam):
    """
    Retrieves and prints the low and high gain tables of the camera.

    Input:
        cam (win32com.client.Dispatch object): 
            The connected camera object.

    Output:
        None
    """
    low_gains = cam.Action(ASCOM_FLI_KEPLER_GET_LOWGAINTABLE, '')
    high_gains = cam.Action(ASCOM_FLI_KEPLER_GET_HIGHGAINTABLE, '')
    
    print('Low Gain Table:')
    print_table(low_gains)
    print('High Gain Table:')
    print_table(high_gains)

def print_table(gains):
    """
    Helper function to print a formatted gain table.

    Input:
        gains (win32com.client.Dispatch object): 
            A collection object containing the gain values (low or high).

    Output:
        None
    """
    for i in range(gains.Count):
        print(f' #{i}, gain={gains[i]}')

def set_gain(cam, low_gain_index, high_gain_index):
    """
    Sets the low and high gains of the camera.

    Input:
        cam (win32com.client.Dispatch object): 
            The connected camera object.
        low_gain_index (int): 
            The index of the low gain setting to apply.
        high_gain_index (int): 
            The index of the high gain setting to apply.

    Output:
        None
    """
    try:
        cam.Action(ASCOM_FLI_KEPLER_SET_LOWGAIN, str(low_gain_index))
        cam.Action(ASCOM_FLI_KEPLER_SET_HIGHGAIN, str(high_gain_index))
        print(f'Set Low Gain: {low_gain_index}, High Gain: {high_gain_index}')
    except com_error as error:
        print(f'Error setting gain: {error}')

def acquire_image(cam, exposure_time=1.0):
    """
    Acquires an image from the camera with a specified exposure time.

    Input:
        cam (win32com.client.Dispatch object): 
            The connected camera object.
        exposure_time (float): 
            The duration of the exposure in seconds. Default is 1.0 second.

    Output:
        image (numpy.ndarray): 
            A 2D numpy array containing the pixel values of the captured image.
    """
    print(f'Acquiring {exposure_time}s exposure...')
    cam.StartExposure(exposure_time, True)
    
    while not cam.ImageReady:
        print('Waiting for image...')
        time.sleep(0.2)
    
    buffer = cam.ImageArray
    image = np.array(buffer, dtype=np.uint16)
    print(f'First pixel: {image[0][0]}')
    return image

def save_image(image, filename="image2.bin"):
    """
    Saves the acquired image to a binary file.

    Input:
        image (numpy.ndarray): 
            A 2D numpy array containing the pixel values of the image to save.
        filename (str): 
            The filename where the image will be saved. Default is 'image2.bin'.

    Output:
        None
    """
    with open(filename, "wb") as newFile:
        newFile.write(image.tobytes())
    print(f'Image saved to {filename}')

def display_image(image):
    """
    Displays the acquired image using matplotlib.

    Input:
        image (numpy.ndarray): 
            A 2D numpy array containing the pixel values of the image to display.

    Output:
        None
    """
    plt.imshow(image, cmap='gray', vmin=0, vmax=4096)
    plt.show()

# Example Usage
if __name__ == "__main__":
    # Connect to the camera
    cam = connect_camera()
    
    # Get camera properties
    get_camera_properties(cam)
    
    # Get available modes
    get_camera_modes(cam)
    
    # Set mode to HDR
    set_camera_mode(cam, 2)
    
    # Get and print gain tables
    get_gain_tables(cam)
    
    # Set Low and High Gains
    set_gain(cam, 2, 7)
    
    # Acquire an image
    image = acquire_image(cam, exposure_time=1.0)
    
    # Save the image to file
    save_image(image)
    
    # Display the image
    display_image(image)
    
    # Disconnect the camera
    disconnect_camera(cam)
