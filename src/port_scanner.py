import socket
import time
from itertools import count
from termcolor import colored

opened_ports = []

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


def scanning():
    global target, port

    print("=" * 15, "Port Scanner", "=" * 15)
    target = input("Enter target IP: ").strip()

    try:
        socket.inet_aton(target)
    except OSError:
        print(colored("Invalid IPv4 address.", "red"))
        return

    print(colored(f"\nTarget: {target}", "red"))
    print(colored("PORT       STATE   SERVICE", "yellow"))

    for port in count(1):
        if port == 1001:
            break
        else:
            port_scanning(target, port)

    if not opened_ports:
        print(colored("No Opened Ports", "blue"))

    print(colored("\nScan completed.", "cyan"))
    time.sleep(3)

scanning()