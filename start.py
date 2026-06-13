import subprocess
import socket
import time
import os
import requests
import os, sys
from os import system
from colorama import Fore, Back, Style
modules = ['requests', 'colorama', 'setuptools', 'tqdm']

def install_module(module):
    try:
        print(f"Installing {module}")
        subprocess.run(["pip3", "install", module], check=True)
    except subprocess.CalledProcessError:
        print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
        sys.exit(1)

for module in modules:
    try:
        __import__(module)
    except ImportError:
        install_module(module)
    except Exception as e:
        print(f"FUCK whats wrong wtf? {e}")
        sys.exit(1)

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
purple = Fore.MAGENTA + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
white = Fore.WHITE + Style.BRIGHT
no_colour = Fore.RESET + Back.RESET + Style.RESET_ALL


def line_print(n):
    for word in n + "\n":
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.05)


# tool version
version = "1.1"

# CHECK INTERNET

socket.setdefaulttimeout(30)


def check_intr(host="8.8.8.8", port=53, timeout=5, retries=3):
    for attempt in range(retries):
        try:
           socket.setdefaulttimeout(timeout)
           socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
           return True
        except socket.error:
           print(f'{red}No internet!Retry {attempt+1}/{retries}')
           time.sleep(2)
    print(f"{red} Where fuckin internet? no after {retries} fuckin exit.")
    sys.exit(1)


def spin():
    delay = 0.25
    spinner = ['€∆∆∆∆', '∆€∆∆∆', '∆∆€∆∆', '∆∆∆€∆', '∆∆∆∆€']

    for _ in range(10):  # Change the range value as per your requirement
        for i in spinner:
            sys.stdout.write(f"\033[34m\r[*] Setting Up Everything.........\033[32m{i}\033[34m\r]")
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write("\b" * (len(i) + 7))
        sys.stdout.write("   \b\b\b\b\b")
        sys.stdout.flush()
    print(" ")
    sys.stdout.write("\033[1;33m [Done]\033[0m")
    sys.stdout.write("\n")

def banner():
    print(f'''
░██████╗░█████╗░███╗░░░███╗██████╗░░█████╗░
██╔════╝██╔══██╗████╗░████║██╔══██╗██╔══██╗
╚█████╗░███████║██╔████╔██║██████╦╝███████║
░╚═══██╗██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
██████╔╝██║░░██║██║░╚═╝░██║██████╦╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝

██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝
''')
    print(f'{yellow}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def check_termux():
    # Install a package using pkg command
    package_name = "proot"
    result = subprocess.run(["pkg", "install", package_name, "-y"], capture_output=True)

    if result.returncode == 0:
        print("Package installation successful.")
    else:
        print("Package installation failed. Error message:")
        print("Trying To Change The Repo")
        os.system(f"echo 'deb https://packages.termux.org/apt/termux-main stable main' >> $PREFIX/etc/apt/sources.list") 
        os.system(f"echo 'deb https://mirror.yandex.ru/termux/apt/termux-main stable main' >> $PREFIX/etc/apt/sources.list")
        os.system(f"echo 'deb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main' >> $PREFIX/etc/apt/sources.list")
        os.system(f"echo 'deb https://ftp.halifax.rwth-aachen.de/termux/apt/termux-main stable main' >> $PREFIX/etc/apt/sources.list")
        os.system(f"echo 'deb https://mirror.ufam.edu.br/termux/apt/termux-main stable main' >> $PREFIX/etc/apt/sources.list")
        os.system("pkg update && pkg upgrade -y")


def update():
    check_intr()
    git_ver = str(
        requests.get(
            "https://raw.githubusercontent.com/GManOfficial/Termux_HackingLab_Setup/main/.version"
        ).text
    ).split()
    if version == git_ver[0]:
        system("clear")
        banner()
        print("Termux_ is up-to-date\n")
    elif version != git_ver and git_ver != "404: Not Found":
        changelog = requests.get(
            "https://raw.githubusercontent.com/GManOfficial/Termux_HackingLab_Setup/main/.changelog.log"
        ).text
        update_commands = requests.get(
            "https://raw.githubusercontent.com/GManOfficial/Termux_HackingLab_Setup/main/.update"
        ).text
        system("clear")
        banner()
        print(
            f"Termux_ has a new update!\nCurrent Version: {red}{version}\nAvailable Version: {green}{git_ver}\n"
        )
        update_ask = input("Do you want to update Termux_?[y/n] > " + green)
        if update_ask == "y":
            print(no_colour)
            system(update_commands)
            line_print(
                "\n"
                + green
                + "Termux_ updated successfully!! Please restart terminal!\n"
            )
            if changelog != "404: Not Found":
                print("Changelog:\n" + purple)
            exit()
        elif update_ask == "n":
            print(
                "\n"
                + "Updating cancelled. Using old version! \nVERSION : "
                + version
            )
            time.sleep(2)
        else:
            print("\nWrong input!\n")
            time.sleep(2)

if __name__ == "__main__":
  try:
    update()
    os.system("clear")
    banner()
    time.sleep(1)
    spin()
    os.system("termux-setup-storage")
    check_termux()

    if os.path.exists("pkg_installer.py"):
        os.system("python3 pkg_installer.py")
    else:
        print(f"{red} Where a file whata kaka?")
        sys.exit(1)

  except KeyboardInterrupt:
    line_print("\n" + green + "Thanks for using This Tool!\n" + no_colour)
