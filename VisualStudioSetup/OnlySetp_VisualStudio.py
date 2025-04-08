import os
import subprocess
import shutil
import platform

# Get VS Code path dynamically
def get_vscode_path():
    """Find the correct path for the VS Code executable."""
    try:
        system = platform.system()
        if system == "Windows":
            result = subprocess.run(["where", "code"], capture_output=True, text=True, check=True)
        else:  # macOS/Linux
            result = subprocess.run(["which", "code"], capture_output=True, text=True, check=True)

        paths = result.stdout.strip().split("\n")

        # Look for a valid executable (prefer `.cmd` on Windows)
        for path in paths:
            path = path.strip()
            if path.endswith("code.cmd") or path.endswith("code.exe") or path.endswith("code"):
                return path

        return None  # No valid executable found

    except subprocess.CalledProcessError:
        return None

# Install extensions from extensions.txt
def install_extensions(vscode_path):
    """Install extensions listed in extensions.txt."""
    extensions_file = "extensions.txt"

    if not os.path.exists(extensions_file):
        print("❌ Error: extensions.txt not found. Please ensure it's in the same directory as this script.")
        return

    with open(extensions_file, "r") as file:
        extensions = [ext.strip() for ext in file.readlines() if ext.strip()]

    for ext in extensions:
        print(f"📦 Installing {ext}...")
        try:
            subprocess.run([vscode_path, "--install-extension", ext], check=True, shell=True)  # <-- Fix applied here
            print(f"✅ Successfully installed: {ext}")
        except subprocess.CalledProcessError:
            print(f"⚠️ Failed to install: {ext}")

# Copy settings.json and keybindings.json
def copy_settings():
    """Copy VS Code settings and keybindings if available."""
    system = platform.system()

    if system == "Windows":
        user_dir = os.path.join(os.getenv('APPDATA'), "Code", "User")
    elif system == "Darwin":
        user_dir = os.path.expanduser("~/Library/Application Support/Code/User")
    elif system == "Linux":
        user_dir = os.path.expanduser("~/.config/Code/User")
    else:
        print("❌ Unsupported operating system.")
        return

    settings_source = "settings.json"
    keybindings_source = "keybindings.json"

    # Ensure the destination directory exists
    os.makedirs(user_dir, exist_ok=True)

    # Copy settings.json
    if os.path.exists(settings_source):
        shutil.copy(settings_source, os.path.join(user_dir, "settings.json"))
        print("✅ Copied settings.json.")

    # Copy keybindings.json
    if os.path.exists(keybindings_source):
        shutil.copy(keybindings_source, os.path.join(user_dir, "keybindings.json"))
        print("✅ Copied keybindings.json.")

# Main setup function
def main():
    vscode_path = get_vscode_path()

    if vscode_path:
        print(f"🔍 Found VS Code at: {vscode_path}")
        install_extensions(vscode_path)
        copy_settings()
        print("🎉 VS Code setup complete!")
    else:
        print("❌ Error: VS Code not found. Ensure it is installed and added to your system PATH.")

if __name__ == "__main__":
    main()
