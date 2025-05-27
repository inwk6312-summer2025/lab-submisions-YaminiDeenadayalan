import yaml
import requests
from requests.auth import HTTPBasicAuth
import json
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

# Credentials (update as needed)
USER = 'student'
PASS = 'Meilab123'

# Read YAML file
with open('routers.yaml', 'r') as f:
    routers = yaml.safe_load(f)['routers']

def set_interface(mgmt_ip, interface, ip_addr):
    url = f"http://{mgmt_ip}/restconf/api/running/interfaces/interface/{interface}"
    auth = HTTPBasicAuth(USER, PASS)
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }
    data = {
        "ietf-interfaces:interface": {
            "name": interface,
            "description": f"Configured by RESTCONF",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": ip_addr,
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }
    try:
        response = requests.put(url, auth=auth, headers=headers, data=json.dumps(data), timeout=5)
        if response.status_code == 204:
            logging.info(f"{mgmt_ip} {interface}: Success")
        else:
            logging.error(f"{mgmt_ip} {interface}: Failed ({response.status_code}) {response.text}")
    except Exception as e:
        logging.error(f"{mgmt_ip} {interface}: Exception {e}")

# Iterate over routers and interfaces
for router in routers:
    mgmt_ip = router['mgmt_ip']
    print(f"mgmtp %s {mgmt_ip}")
    for interface, ip_addr in router['interfaces'].items():
        set_interface(mgmt_ip, interface, ip_addr)

