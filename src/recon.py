import socket
import time
import subprocess
import logging
from pathlib import Path
from termcolor import colored

# logs
logs_file = Path(__file__).resolve().parent.parent / "logs" / "recon.log"

logger = logging.getLogger("Reconnaissance")
file_h = logging.FileHandler(logs_file)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_h.setFormatter(formatter)

logger.addHandler(file_h)
logger.setLevel(logging.INFO)

#DNS Resolver
def dns():
    try:
        targetDomain = input("Enter domain: ")
        hostname = socket.gethostbyname(targetDomain)
        logger.info(f"DNS resolving succeeded on '{targetDomain}' -> '{hostname}'")
        return {
            "Target": targetDomain,
            "Resolved IP": hostname,
            "Status": "Success"
        }
    except socket.gaierror:
        logger.error(f"DNS resolving failed on '{targetDomain}' -> NULL")
        return {
            "Target": targetDomain,
            "Resolved IP": None,
            "Status": "Failed"
        }

#Target validation
def validate_target():
    print("=" * 15)
    print("[1] IP | [2] Host name")
    choice = str(input("Do you have an IP or a hostname?: "))

    if choice == "1":
        try:
            ipaddr = input("Enter IP: ")
            socket.gethostbyaddr(ipaddr)
            print(f"'{ipaddr}' was validated and found successfully!")
            logger.info(f"'{ipaddr}' validated and found")
        except socket.gaierror:
            print(f"'{ipaddr}' was not found")
            logger.error(f"'{ipaddr}' was not found")
        except:
            print(f"oops... Seems like there's an issue")
            logger.error("an error occured during validation")

    elif choice == "2":
        try:
            hostname = input("Enter hostname: ")
            socket.gethostbyaddr(hostname)
            print(f"'{hostname}' was validated and found successfully!")
            logger.info(f"'{hostname}' was validated and found")
        except socket.gaierror:
            print(f"'{hostname}' was not found")
            logger.error(f"'{hostname}' was not found")
        except:
            print(f"oops... Seems like there's an issue")
            logger.error("an error occured during validation")
    else:
        print("Invalid choice")

#Web headers
def web_headers():
    url = input("Enter URL: ")
    headers = subprocess.run(["curl", "-I", url], capture_output=True, text=True)

    if headers.returncode == 22:
        print(headers)
        logger.info(f"headers of '{url}' was retrieved successfully")
    else:
        print(colored(f"Could retrieve '{url}' headers", "red"))
        logger.error(f"Could retrieve '{url}' headers")


def Reconnaissance():
    print("=" * 15, "Target Reconnaissance", "=" * 15)
    print("[1] Resolve DNS")
    print("[2] Validate Target")
    print("[3] Web Headers")
    print("=" * 15)
    choice = str(input("Service?: "))

    if choice == "1":
        print(dns())
    elif choice == "2":
        validate_target()
    elif choice == "3":
        web_headers()
    else:
        print("Enter a valid choice")
        time.sleep(1.5)