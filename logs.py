import json
import os

def load_reports():
    reports_file = "/home/eyaddoo/vscode/python/RedOps/data/reports.json"
    with open(reports_file, "r") as file:
        json.load(file)


def port_scanner_saved_reports(targets, ports):
    reports_file = "/home/eyaddoo/vscode/python/RedOps/data/reports.json"
    data = {"Target": targets, "Ports": [ports]}
    written_data = json.dumps(data, indent=4)

    with open(reports_file, "w") as file:
        file.write(written_data)


def recon_saved_reports(recon_id):
    reports_file = "/home/eyaddoo/vscode/python/RedOps/data/reports.json"
    tool = ""

    if recon_id == 1:
        tool = "Resolve DNS"
    elif recon_id == 2:
        tool = "Validate Target"
    elif recon_id == 3:
        tool = "Web Headers"

    data = {"Recon_ID": recon_id, "Tool": tool}
    written_data = json.dumps([data], indent=4)
    with open(reports_file, "w") as file:
        file.write(written_data)


def content_discovery_saved_reports(hostname, endpoints):
    reports_file = "/home/eyaddoo/vscode/python/RedOps/data/reports.json"
    data = {"Hostname": hostname, "Endpoints": [endpoints]}
    written_data = json.dumps([data], indent=4)

    if os.path.getsize(reports_file) == 0:
        with open(reports_file, "w") as file:
            file.write(written_data)
        with open(reports_file, "a+") as file:
            file.write(",")
    else:
        with open(reports_file, "a") as file:
            file.write(written_data)

        with open(reports_file, "a+") as file:
            file.write(",")