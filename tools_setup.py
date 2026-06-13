from colorama import Fore, Back, Style
import subprocess
import socket
import time
import os
import os, sys
from os import system

red = Fore.RED + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
no_colour = Fore.RESET + Back.RESET + Style.RESET_ALL

def line_print(n):
    for word in n + "\n":
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.05)

def sqlmap():
  try:
    print(f"{yellow} Начинаем скачивать sqlmap...")
    print(f"{red} Юзайте только на своем!..")
    answer = input(f"Продолжить? (y/n)")
    if answer.lower() == 'y':
        os.system("cd $HOME && git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
        print(f"{green}✅ sqlmap installed to ~/sqlmap-dev")
    else:
        print(f"{red}❌ sqlmap installation cancelled")
  except Exception as e:
      print(f"{red} errno: {e}")

def proxy():
  try:
    print(f"{yellow}  Начинаем скачивание фри-прокси...")
    print(f"{red} Прокси могут небезопасны..")
    answer = input(f"Продолжить? (y/n)")
    if answer.lower() == 'y':
        subprocess.run(["git","clone","https://github.com/mishakorzik/Free-Proxy", "~/Free-Proxy"])
        print(f"{green}✅ Free-Proxy installed to ~/Free-Proxy")
    else:
        print(f"{red}❌ Free-Proxy installation cancelled")
  except Exception as e:
      print(f"{red} Errno: {e}")


if __name__ == '__main__':
  try:
       os.system("clear")
       print(f"{green}1. Установить sqlmap (тестирование SQL-инъекций)")
       print(f"{green}2. Установить Free-Proxy (список прокси)")
       print(f"{yellow}0. Выйти")
       choice = input(f"{cyan}Выберите опцию: ")
       if choice == '1':
           sqlmap()
       elif choice == '2':
           proxy()
       else:
           print(f"{red}Выход...")
  except KeyboardInterrupt:
       line_print("\n" + green + "Thanks for using This Tool!\n" + no_colour)
