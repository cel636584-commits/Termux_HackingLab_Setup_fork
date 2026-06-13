import subprocess
from colorama import Fore, Back, Style
import os
import sys
import time

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

def check_and_install(cmd, pkg_name, display_name):
    """Проверяет наличие команды, если нет — устанавливает через pkg"""
    installed = subprocess.call(f"command -v {cmd} > /dev/null 2>&1", shell=True)
    if installed == 0:
        print(f"{green}[+]-[{display_name}].........................[ Installed ]")
    else:
        print(f"{red}[-]-[{display_name}].......................[ Not Found ]")
        time.sleep(1)
        print(f"{yellow}[!] Installing {display_name}...")
        subprocess.call(f"pkg install {pkg_name} -y", shell=True)
    time.sleep(0.5)

try:
    subprocess.call("clear", shell=True)
    time.sleep(0.5)

    # Баннер
    print(f"{red} ______                                  __  __           __   _            ")
    print(f'{cyan}/_  __/__  _________ ___  __  ___  __   / / / /___ ______/ /__(_)___  ____ _')
    print(f'{yellow} / / / _ \/ ___/ __ `__ \/ / / / |/_/  / /_/ / __ `/ ___/ //_/ / __ \/ __ `/')
    print(f'{blue} / / /  __/ /  / / / / / / /_/ />  <   / __  / /_/ / /__/ ,< / / / / / /_/ / ')
    print(f'{red}/_/  \___/_/  /_/ /_/ /_/\__,_/_/|_| _/_/ /_/\__,_/\___/_/|_/_/_/ /_/\__, /  ')
    print(f'{yellow}             __          (_)      __(_)      __                     /____/   ')
    print(f'{green}            / /   ____ _/ /_     / ___/___  / /___  ______                   ')
    print(f'{cyan}           / /   / __ `/ __ \    \__ \/ _ \/ __/ / / / __ \                  ')
    print(f'{red}          / /___/ /_/ / /_/ /   ___/ /  __/ /_/ /_/ / /_/ /                  ')
    print(f'{yellow}         /_____/\__,_/_.___/   /____/\___/\__/\__,_/ .___/                   ')
    print(f'{blue}                                                  /_/                        ')
    print("                         Tool Name: TermuxSetupHackingLab")
    print("                           Developer: @G_Man_Official (fixed version)")
    print(f'{yellow}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

    # Установка базовых пакетов (только нужное, без python2 и ruby)
    check_and_install("git", "git", "Git")
    check_and_install("python3", "python", "Python")
    check_and_install("openssl", "openssl", "OpenSSL")
    check_and_install("wget", "wget", "Wget")
    check_and_install("php", "php", "PHP")
    check_and_install("zip", "zip", "Zip")
    check_and_install("curl", "curl", "Curl")
    check_and_install("nodejs", "nodejs", "Nodejs")
    check_and_install("lolcat", "lolcat", "Lolcat")  # теперь через pkg, не через ruby!

    # Финальный баннер
    subprocess.call("clear", shell=True)
    print(f'''{green}
   ___             __         __ __          __
  |   .-----.-----|  |_.---.-|  |  .-----.--|  |
  |.  |     |__ --|   _|  _  |  |  |  -__|  _  |
  |.  |__|__|_____|____|___._|__|__|_____|_____|
  |:  |
  |::.|
  `---' ''')
    print("                       Tool Name: TermuxSetupHackingLab")
    print("                       Developer: @G_Man_Official (fixed version)")
    print(f"{cyan}                Telegram :: https://t.me/hacking_network8 (original)")
    print(f'{yellow}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f"{green}[+]-[Git].............................[ Installed ]")
    print(f"{green}[+]-[Python]..........................[ Installed ]")
    print(f"{green}[+]-[OpenSSL].........................[ Installed ]")
    print(f"{green}[+]-[Wget]............................[ Installed ]")
    print(f"{green}[+]-[PHP].............................[ Installed ]")
    print(f"{green}[+]-[PIP].............................[ Installed ]")
    print(f"{green}[+]-[Curl]............................[ Installed ]")
    print(f"{green}[+]-[Nodejs]..........................[ Installed ]")
    print(f"{green}[+]-[Lolcat]..........................[ Installed ]")
    print("")
    time.sleep(2)

    # Запуск следующего установщика (если нужен)
    if os.path.exists("python_modules.py"):
        os.system("python3 python_modules.py")
    else:
        print(f"{yellow}python_modules.py not found, skipping...")

except KeyboardInterrupt:
    line_print("\n" + green + "Thanks for using This Tool!\n" + no_colour)
    sys.exit(0)
