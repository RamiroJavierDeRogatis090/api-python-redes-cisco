import csv
import requests

BASE_URL = "http://localhost:58000/api/v1"
AUTH = {"username": "admin", "password": "Admin1234"}

r_ticket = requests.post(f"{BASE_URL}/ticket", json=AUTH)
r_ticket.raise_for_status()
ticket = r_ticket.json()["response"]["serviceTicket"]
headers = {"X-Auth-Token": "NC-8-4ef04827cb8347a1832f-nbi"}

devices = requests.get(f"{BASE_URL}/network-device", headers=headers).json().get("response", [])
hosts = requests.get(f"{BASE_URL}/host", headers=headers).json().get("response", [])

with open("inventario_red.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tipo", "Nombre", "IP", "Estado / Ping", "Conectado a / Modelo"])
    for d in devices:
        writer.writerow([
            "Dispositivo",
            d.get("hostname", ""),
            d.get("managementIpAddress", ""),
            d.get("collectionStatus", ""),
            d.get("platformId", "")
        ])
    for h in hosts:
        writer.writerow([
            f"Host ({h.get('hostType', '')})",
            h.get("hostName", ""),
            h.get("hostIp", ""),
            h.get("pingStatus", ""),
            f"{h.get('connectedNetworkDeviceName', '')} ({h.get('connectedInterfaceName', '')})"
        ])

print(f"Exportados {len(devices)} dispositivos y {len(hosts)} hosts a inventario_red.csv")


