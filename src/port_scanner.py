import socket
import time
import logging
from pathlib import Path
from itertools import count
from termcolor import colored

# logs
logs_file = Path(__file__).resolve().parent.parent / "logs" / "scanning.log"

logger = logging.getLogger("Port Scanner")
file_h = logging.FileHandler(logs_file)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_h.setFormatter(formatter)

logger.addHandler(file_h)
logger.setLevel(logging.INFO)


opened_ports = []

# port scanning codes

def port_scanning(target, port):
    try:
        service = socket.getservbyport(port, "tcp")
    except OSError:
        service = "UNKNOWN"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_sock:
            tcp_sock.settimeout(0.5)
            result = tcp_sock.connect_ex((target, port))

        if result == 0:
            print(colored(f"[+] {port}/tcp  OPEN  {service}", "green"))
            opened_ports.append(port)

    except (socket.gaierror, OSError) as error:
        print(colored(f"Error scanning {target}:{port}: {error}", "red"))
        logger.error(f"Error scanning {target}:{port}:{error}")

# scanning

def scanning():
    global target, port

    print("=" * 15, "Port Scanner", "=" * 15)
    target = input("Enter target IP: ").strip()

    try:
        socket.inet_aton(target)
    except OSError:
        print(colored("Invalid IPv4 address.", "red"))
        logger.error("Invalid IPv4 address")
        return

    logger.info(f"Scanning {target}")
    print(colored(f"\nTarget: {target}", "red"))
    print(colored("PORT       STATE   SERVICE", "yellow"))

    for port in count(1):
        if port == 1001:
            break
        else:
            port_scanning(target, port)

    if not opened_ports:
        print(colored("No Opened Ports", "blue"))
        logger.info(f"No opened ports on {target}")

    print(colored("\nScan completed.", "cyan"))
    logger.info("Scan Completed")
    time.sleep(3)