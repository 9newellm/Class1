import subprocess
import sys
import os
import winreg as reg

""" Step 1. Requirequirments to run as an adminstraotr and install all the necesary software"""

def check_dotnet_version(version):
    try:
        # Open the registry key for the .NET Framework versions
        reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full")
        # Retrieve the version value
        installed_version, _ = reg.QueryValueEx(reg_key, "Version")
        reg.CloseKey(reg_key)
        # Compare with the required version
        return installed_version >= version
    except FileNotFoundError:
        return False

def enable_dotnet_framework(version):
    try:
        # Convert version to a string format compatible with DISM
        version_str = f"{version[0]}.{version[1]}"
        # Run DISM to enable the .NET Framework feature
        subprocess.run(
            ["dism", "/online", "/enable-feature", f"/featurename:NetFx{version_str}", "/all", "/norestart"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f".NET Framework {version_str} enabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error enabling .NET Framework {version_str}: {e}")
        sys.exit(1)

def register_dll(dll_path):
    try:
        # Run regsvr32 to register the DLL
        subprocess.run(
            ["regsvr32", "/s", dll_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"Registered {dll_path} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error registering {dll_path}: {e}")
        sys.exit(1)

def main():
    # Define the required .NET Framework version
    required_version = (4, 8)
    # Define the path to mscoree.dll
    mscoree_dll_path = r"C:\Windows\System32\mscoree.dll"

    # Check if the required .NET Framework version is installed
    if not check_dotnet_version(required_version):
        print(f".NET Framework {'.'.join(map(str, required_version))} is not installed.")
        enable_dotnet_framework(required_version)
    else:
        print(f".NET Framework {'.'.join(map(str, required_version))} is already installed.")

    # Register mscoree.dll
    if os.path.exists(mscoree_dll_path):
        register_dll(mscoree_dll_path)
    else:
        print(f"{mscoree_dll_path} not found.")

if __name__ == "__main__":
    main()
