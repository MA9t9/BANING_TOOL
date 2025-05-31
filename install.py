
'''          CODE BY  𐏓꯭  𝗠𝗥ᬊ͜͡  M A LEGEND〆͎          '''

import os
import subprocess
import sys
import time

def install_packages():
    packages = ["webbrowser", "urllib.parse"]
    pip = "pip3" if sys.version_info[0] == 3 else "pip"
    
    try:
        subprocess.run([pip, "install", "--upgrade", "pip"], check=True)
        for pkg in packages:
            subprocess.run([pip, "install", pkg], check=False)
    except Exception as e:
        print(f"Error installing packages: {e}")

if __name__ == "__main__":
    os.system("clear")
    print("Installing required packages...")
    time.sleep(1)
    install_packages()
    print("Launching tool...")
    time.sleep(1)
    os.system("python3 main.py" if sys.version_info[0] == 3 else "python main.py")