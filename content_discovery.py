import socket
import requests
from termcolor import colored
from logs import content_discovery_saved_reports, load_reports

def discovering():
    wordlists_path = "/home/eyaddoo/vscode/python/RedOps/wordlists/wordlists.txt"
    print("=" * 15, "Web Endpoints Discovery", "=" * 15)

    try:
        hostname = input("Enter hostname (no schemes 'port/https/http/queries'): ").strip()
        socket.gethostbyname(hostname)

        with open(wordlists_path, "r") as file:
            print(colored("Processing...", "magenta"))

            for i, words in enumerate(file, start=1):
                endpoints = "https://" + hostname + "/" + words.strip()
                response = requests.get(endpoints)

                if response.status_code == 401:
                    print(colored(f"{i}/4756: Unauthorized {endpoints}", "yellow"))
                elif response.status_code == 403:
                    print(colored(f"{i}/4756: Forbidden {endpoints}", "orange"))
                elif response.status_code == 200:
                    print(colored(f"{i}/4756: Found {endpoints}", "green"))
                    content_discovery_saved_reports(hostname, endpoints)
                    load_reports()

        print()
        print(colored("Discovering Completed", "cyan"))
        
    except socket.gaierror:
        print(f"'{hostname}' was not found")
    except:
        print()
        print("Oops... Something went wrong please try again")

# discovering()