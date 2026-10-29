import socket
import requests
from termcolor import colored

def discovering():
    wordlists_path = "/src/wordlists/wordlists.txt"
    print("=" * 15, "Web Endpoints Discovery", "=" * 15)

    try:
        hostname = input("Enter hostname (no schemes 'port/https/http/queries'): ").strip()
        socket.gethostbyname(hostname)

        with open(wordlists_path, "r") as file:
            print(colored(f"Scanning file...", "magenta"))

            for words in file:
                endpoints = "https://" + hostname + "/" + words.strip()
                response = requests.get(endpoints, timeout=5, allow_redirects=True)

                if response.status_code == 401:
                    print(colored(f"[-] 401 Unauthorized: {endpoints}", "yellow"))
                elif response.status_code == 403:
                    print(colored(f"[-] 403 Forbidden: {endpoints}", "red"))
                elif response.status_code == 200:
                    print(colored(f"[+] 200 Found: {endpoints}", "green"))
                elif response.status_code == "301":
                    print(colored(f"[+] 301 Redirected: {endpoints}", "blue"))
                elif response.status_code == "302":
                    print(colored(f"[+] 302 Found: {endpoints}", "light_blue"))
 
        print()
        print(colored("Discovering Completed", "cyan"))
        
    except socket.gaierror:
        print(f"'{hostname}' was not found")
    except KeyboardInterrupt:
        print("\nOops... Keyboard interrupt was found")
    except requests.exceptions.RequestException:
        pass
    except FileNotFoundError:
        print(f"Wordlists file not found at {wordlists_path}")