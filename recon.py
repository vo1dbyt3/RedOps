import socket
import time
import subprocess
from logs import recon_saved_reports
from termcolor import colored

def dns():
    try:
        targetDomain = input("Enter domain: ")
        hostname = socket.gethostbyname(targetDomain)
        return {
            "Target": targetDomain,
            "Resolved IP": hostname,
            "Status": "Success"
        }
    except socket.gaierror:
        return {
            "Target": targetDomain,
            "Resolved IP": None,
            "Status": "Failed"
        }

def validate_target():
    print("=" * 15)
    print("[1] IP | [2] Host name")
    choice = str(input("Do you have an IP or a hostname?: "))

    if choice == "1":
        try:
            ipaddr = input("Enter IP: ")
            socket.gethostbyaddr(ipaddr)
            print(f"'{ipaddr}' was validated and found successfully!")
        except socket.gaierror:
            print(f"'{ipaddr}' was not found")
        except:
            print(f"oops... Seems like there's an issue")
    elif choice == "2":
        try:
            hostname = input("Enter hostname: ")
            socket.gethostbyaddr(hostname)
            print(f"'{hostname}'was validated and found successfully!")
        except socket.gaierror:
            print(f"'{hostname}' was not found")
        except:
            print(f"oops... Seems like there's an issue")
    else:
        print("Invalid choice")

def web_headers():
    url = input("Enter URL: ")
    headers = subprocess.run(["curl", "-I", url])
    print(headers)

def unknown3():
    pass

def Reconnaissance():
    print("=" * 15, "Target Reconnaissance", "=" * 15)
    print("[1] Resolve DNS")
    print("[2] Validate Target")
    print("[3] Web Headers")
    print("=" * 15)
    choice = str(input("Service?: "))

    if choice == "1":
        recon_id_1 = 1
        print(dns())
        recon_saved_reports(recon_id_1)
    elif choice == "2":
        recon_id_2 = 2
        validate_target()
        recon_saved_reports(recon_id_2)
    elif choice == "3":
        recon_id_3 = 3
        web_headers()
        recon_saved_reports(recon_id_3)
    else:
        print("Enter a valid choice")
        time.sleep(1.5)

# Reconnaissance()