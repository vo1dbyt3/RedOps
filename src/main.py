from menu import show_menu
from recon import Reconnaissance
from port_scanner import scanning
from content_discovery import discovering
from details import details_note
from termcolor import colored
import time
import os

file_path = "/home/eyaddoo/vscode/python/RedOps/data/reports.json"

def main():
    operating = True

    try:
        while operating:
            show_menu()
            choice = str(input("Operation: "))

            if choice == "1":
                time.sleep(1)
                Reconnaissance()
            elif choice == "2":
                time.sleep(1)
                scanning()
            elif choice == "3":
                time.sleep(1)
                discovering()
            elif choice == "4":
                time.sleep(1)

                if os.path.getsize(file_path) == 0:
                    print(colored("No available data", "red"))
                else:
                    with open(file_path, "r") as file:
                        contents = file.read()
                        print(contents)
                        
            elif choice == "5":
                time.sleep(1)
                details_note()
            elif choice == "6":
                operating = False
            else:
                print("Please enter a valid operation")
                print()
                time.sleep(1.5)
    except:
        print()
        print("Oops... Something went wrong" "\n" "Please try operating once again")

if __name__ == "__main__":
    main()