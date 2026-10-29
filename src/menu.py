import pyfiglet
from termcolor import colored

def show_menu():
    ascii_text = pyfiglet.figlet_format("RedOps", font="slant")

    print("=" * 28)
    print(colored(ascii_text, "red"))
    print("=" * 28)
    print("[1] Target Reconnaissance")
    print("[2] Port Scanner")
    print("[3] Web Endpoints Discovery")
    print("[4] Help?")
    print("[5] Exit")
    print("=" * 28)