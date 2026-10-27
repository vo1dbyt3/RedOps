from termcolor import colored

def recon():
    print(colored("DNS Resolution:", "red"))
          
    print(colored(
    "Resolves a domain name to an IPv4 address using\n"
    "socket.gethostbyname(). Returns the target domain,\n"
    "resolved IP address, and operation status. Does not\n"
    "enumerate DNS records such as MX, NS, or TXT.\n\n", "yellow"))

    
    print(colored("Target Validation:", "red"))

    print(colored(
    "Attempts a reverse DNS lookup using socket.gethostbyaddr()\n"
    "to check whether an IP address or hostname can be resolved\n"
    "to a hostname. This is not complete target validation,\n"
    "and a failed reverse lookup does not necessarily mean\n"
    "the target is invalid.\n\n", "yellow"))


    print(colored("Web Headers:", "red"))
    print(colored(
    "Uses subprocess.run() to execute curl -I against a supplied\n"
    "URL to retrieve HTTP response headers without downloading\n"
    "the response body. Headers are printed by curl and are\n"
    "not analyzed or saved by this operation.\n\n", "yellow"))


def port_scanner(): 
    print(colored("TCP Port Scanner"" Scans TCP ports 1 through 1000 on a target IPv4 address.\n"
    "Uses Python sockets and connect_ex() to test whether\n"
    "connections can be established. Displays reachable ports.\n"
    "Closed ports are not displayed, and\n"
    "the scanner does not perform vulnerability detection", "yellow"))
    

def web_endpoints():
    print(colored("Web Endpoint Discovery:", "red"))
    print(colored(
    "Tests candidate web paths from a local wordlist against\n"
    "an HTTPS hostname using requests.get(). Displays endpoints\n"
    "that return HTTP 200 (Found), 401 (Unauthorized), or\n"
    "403 (Forbidden). Requires a valid hostname, a readable\n"
    "wordlist file, and the requests and termcolor packages.\n"
    "Only HTTPS is tested. Other HTTP status codes are ignored,", "yellow"))

def details_note():
    reading = True

    while reading:
        print("=" * 15, "Details menu", "=" * 15)
        print("[1] Target Reconnaissance")
        print("[2] Port Scanner")
        print("[3] Web Endpoints Discovery")
        print("[4] Back to Menu")
        print("=" * 28)

        try:
            choice = str(input("Which operation do u wanna get details about?: "))

            if choice == "1":
                recon()
            elif choice == "2":
                port_scanner()
            elif choice == "3":
                web_endpoints()
            elif choice == "4":
                reading = False
            else:
                pass
        except:
            print()
            print("Oops... Something went wrong" "\n" "Please try again")

# details_note()