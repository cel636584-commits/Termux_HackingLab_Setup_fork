import subprocess
import os
import sys
from os import system

modules = ['requests', 'colorama', 'setuptools', 'tqdm']

def install_module(module):
    try:
        os.system("pkg update && pkg upgrade -y")
        print(f"Installing {module}")
        subprocess.run(["pip3", "install", module], check=True)
    except subprocess.CalledProcessError:
        print(f"{module} cannot be installed! Install it manually by 'pip3 install {module}'")
        sys.exit(1)

for module in modules:
    try:
        __import__(module)
    except ImportError:
        install_module(module)
    except Exception as e:
        print(f"where a {module} dear?") 
        sys.exit(1) 


# Install a package using pkg command
    package_name = "proot"
    result = subprocess.run(["pkg", "install", package_name, "-y"], capture_output=True)

    if result.returncode == 0:
        print("Пакеты установлены...")
    else:
        print("Package installation failed. Error message:")
        print("Trying To Change The Repo")
        os.system(f"echo 'deb https://packages.termux.org/apt/termux-main stable main' >> $PREFIX/etc/apt/sources.list")
        os.system(f"echo 'deb https://mirror.yandex.ru/termux/apt/termux-main stable main' >> $PREFIX/etc/apt/sources.list") 
        os.system(f"echo 'deb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main' >> $PREFIX/etc/apt/sources.list") 
        os.system(f"echo 'deb https://ftp.halifax.rwth-aachen.de/termux/apt/termux-main stable main' >> $PREFIX/etc/apt/sources.list")
        os.system(f" echo 'deb https://mirror.ufam.edu.br/termux/apt/termux-main stable main' >> $PREFIX/etc/apt/sources.list")
        os.system("python3 start.py") 
