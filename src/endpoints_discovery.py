import socket
import requests
import logging
from termcolor import colored
from pathlib import Path

# logs
logs_file = Path(__file__).resolve().parent.parent / "logs" / "endpoints.log"

logger = logging.getLogger("Endpoints Discovery")
file_h = logging.FileHandler(logs_file)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_h.setFormatter(formatter)

logger.addHandler(file_h)
logger.setLevel(logging.INFO)

def discovering():
    wordlists_path = Path(__file__).resolve().parent.parent / "src" / "wordlists" / "wordlists.txt"
    print("=" * 15, "Web Endpoints Discovery", "=" * 15)

    try:
        hostname = input("Enter hostname (no schemes 'port/https/http/queries'): ").strip()
        socket.gethostbyname(hostname)

        with open(wordlists_path, "r") as file:
            print(colored(f"Scanning file...", "magenta"))
            logger.info(f"Scanning '{hostname}'")

            for words in file:
                endpoints = "https://" + hostname + "/" + words.strip()
                response = requests.get(endpoints, timeout=5, allow_redirects=True)

                if response.status_code == 401:
                    print(colored(f"[-] 401 Unauthorized: {endpoints}", "yellow"))
                    logger.warning(f"Unauthorized: '{endpoints}'")
                elif response.status_code == 403:
                    print(colored(f"[-] 403 Forbidden: {endpoints}", "red"))
                    logger.warning(f"Forbidden: '{endpoints}'")
                elif response.status_code == 200:
                    print(colored(f"[+] 200 Found: {endpoints}", "green"))
                    logger.info(f"Found: '{endpoints}'")
                elif response.status_code == 301:
                    print(colored(f"[+] 301 Redirected: {endpoints}", "blue"))
                    logger.info(f"Redirected: '{endpoints}'")
                elif response.status_code == 302:
                    print(colored(f"[+] 302 Found & Temporarily Moved: {endpoints}", "light_blue"))
                    logger.info(f"Found & Temporarily Moved: '{endpoints}'")

        print(colored("\nDiscovering Completed", "cyan"))
        logger.info(f"Discovering '{hostname}' endpoints completed")
        
    except socket.gaierror:
        print(f"'{hostname}' was not found")
        logger.error(f"'{hostname}' was not found")
    except KeyboardInterrupt:
        print("\nOops... Keyboard interrupt was found")
        logger.error("'KeyboardIntterupt' error occured")
    except requests.exceptions.RequestException as error:
        logger.error(f"error occured: {error}")
        pass
    except FileNotFoundError:
        print(f"Wordlists file not found at {wordlists_path}")
        logger.error(f"'{wordlists_path}' doesn't exist")