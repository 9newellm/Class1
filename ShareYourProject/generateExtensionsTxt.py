import subprocess
import os

def get_vscode_path():
    """Find the correct path for VS Code's command-line tool."""
    try:
        # Run 'where code' and capture the output
        result = subprocess.run(["where", "code"], capture_output=True, text=True, check=True)
        paths = result.stdout.strip().split("\n")  # Handle multiple results

        # Look for 'code.cmd' explicitly
        for path in paths:
            if path.strip().endswith("code.cmd"):
                return path.strip()

        # Fallback to the first result if 'code.cmd' isn't found
        return paths[0].strip() if paths else None

    except subprocess.CalledProcessError:
        print("Error: VS Code not found in PATH. Ensure it's installed and added to system PATH.")
        return None

def generate_extension_list():
    vscode_path = get_vscode_path()
    
    if not vscode_path:
        print("Error: Could not find a valid VS Code executable.")
        return

    try:
        setup_folder = os.path.join(os.getcwd(), "VisualStudioSetup")
        os.makedirs(setup_folder, exist_ok=True)

        # Run the VS Code command using the correct path
        result = subprocess.run([vscode_path, "--list-extensions"], capture_output=True, text=True, check=True)

        extensions_file_path = os.path.join(setup_folder, "extensions.txt")
        with open(extensions_file_path, "w") as file:
            file.write(result.stdout)

        print(f"Extensions list saved to {extensions_file_path}")

    except subprocess.CalledProcessError:
        print("Error: Unable to list extensions. Ensure VS Code is installed and configured properly.")
    except FileNotFoundError:
        print("Error: The specified VS Code path is incorrect. Please check it.")

if __name__ == "__main__":
    generate_extension_list()
