import socket
import time
import os
import json
from logs import port_scanner_saved_reports
from termcolor import colored

json_file = "/home/eyaddoo/vscode/python/RedOps/data/reports.json"
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

    print()
    print(colored(f"Target: {target}", "red"))
    print(colored("PORT       STATE   SERVICE", "yellow"))

    for port in range(1, 1001):
        port_scanning(target, port)

    if os.path.getsize(json_file) == 0:
        port_scanner_saved_reports(target, opened_ports)
    else:
        with open(json_file, "r") as file:
            existing = json.load(file)

        if not isinstance(existing, dict):
            existing = {}

        existing.update({"Ports": opened_ports, "Target": target})

        with open(json_file, "w") as file:
            json.dump(existing, file, indent=2)

    if opened_ports == []:
        print(colored("No Opened Ports", "blue"))

    print()
    print(colored("Scan completed.", "cyan"))
    time.sleep(3)

# scanning()