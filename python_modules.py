import subprocess
import sys

modules = ['requests','colorama']

for module in modules:
    try:
        __import__(module)
        print(f"{module} уже установлен.")
    except ImportError:
        print(f"Устанавливаю...")
        subprocess.run([sys.executable, "-m","pip","install", module])
        print(f"{module} установлен, ёпт.")

if __name__ == '__main__':
    import os
    if os.path.exists("tools_setup.py"):
        os.system("python3 tools_setup.py")
