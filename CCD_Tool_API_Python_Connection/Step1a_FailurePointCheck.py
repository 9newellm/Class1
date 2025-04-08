import ctypes
import os

# Define the expected paths for mscoree.dll
possible_paths = [
    r"C:\Windows\System32\mscoree.dll",
    r"C:\Windows\SysWOW64\mscoree.dll"
]

loaded = False
for path in possible_paths:
    if os.path.exists(path):
        try:
            # Try loading the DLL
            mscoree = ctypes.WinDLL(path)
            print(f"Successfully loaded mscoree.dll from {path}")
            loaded = True
            break
        except Exception as e:
            print(f"Error loading mscoree.dll from {path}: {e}")

if not loaded:
    print("mscoree.dll could not be loaded from any of the expected locations.")
    print("necessary dependecy will limit application from working")
