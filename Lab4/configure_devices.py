import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

# Load YAML
with open("devices.yml") as f:
    devices = yaml.safe_load(f)

# Setup Jinja
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.j2")

# Configure all routers
for router in devices['all_routers']:
    config = template.render(**router)
    print(f"Configuring {router['name']}")

    connection = ConnectHandler(
        device_type=router["device_type"],
        host=router["hostname"],
        username=router["username"],
        password=router["password"]
    )
    connection.send_config_set(config.splitlines())
    connection.disconnect()

