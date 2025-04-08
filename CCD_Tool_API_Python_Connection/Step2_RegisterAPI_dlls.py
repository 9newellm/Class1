import os
import sys
import subprocess

def get_regasm_path():
    """
    Returns the path to RegAsm.exe based on the OS architecture.
    We'll use the 32-bit version (Framework) as given in your example.
    For a 64-bit process you may also use the Framework64 folder.
    """
    # Change this if you need to use the 64-bit version.
    return r"C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegAsm.exe"

def register_dll(dll_path, regasm_path):
    """
    Register a given DLL using RegAsm.exe with /codebase and /tlb options.
    """
    # Build the command; note that /s runs it silently.
    command = [regasm_path, dll_path, "/codebase", "/tlb"]
    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"SUCCESS: Registered {dll_path}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"FAILED: Registration of {dll_path} returned error:")
        print(e.stderr)

def main():
    # Get the current working directory (the project's base directory)
    current_dir = os.getcwd()

    # Set the base folder dynamically to include the current directory
    base_folder = os.path.join(current_dir, "ASCOM-Python-Programming")
    
    if not os.path.isdir(base_folder):
        print(f"Error: The folder '{base_folder}' does not exist.")
        sys.exit(1)

    # Get the RegAsm.exe path:
    regasm_path = get_regasm_path()
    if not os.path.isfile(regasm_path):
        print(f"Error: RegAsm.exe was not found at '{regasm_path}'.")
        sys.exit(1)

    # List all DLL files in the specified folder.
    dll_files = [f for f in os.listdir(base_folder) if f.lower().endswith(".dll")]

    if not dll_files:
        print("No DLL files found in the folder.")
        sys.exit(0)

    print("Starting registration of DLLs in folder:")
    print(base_folder)
    print("-" * 50)

    for dll in dll_files:
        dll_path = os.path.join(base_folder, dll)
        print(f"Registering {dll_path}...")
        register_dll(dll_path, regasm_path)

    print("DLL registration process completed.")

if __name__ == "__main__":
    main()
