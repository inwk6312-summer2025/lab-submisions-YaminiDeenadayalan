from netmiko import ConnectHandler
import yaml
from textfsm import clitable

# Load YAML
with open("devices.yml") as f:
    devices = yaml.safe_load(f)

# CLI Table for parsing
cli_table = clitable.CliTable('ntc-templates/ntc_templates/index', 'ntc-templates/ntc_templates/templates')

for router in devices['all_routers']:
    try:
        connection = ConnectHandler(
            device_type=router["device_type"],
            host=router["hostname"],
            username=router["username"],
            password=router["password"]
        )

        output = connection.send_command("show ip route")
        connection.disconnect()

        attributes = {"Command": "show ip route", "Platform": "cisco_ios"}
        cli_table.ParseCmd(output, attributes)

        print(f"Routing Table for {router['name']}:")
        for row in cli_table:
            print(dict(zip(cli_table.header, row)))

    except Exception as e:
        print(f"Error collecting routing table from {router['name']}: {e}")

