
import logging
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

# Setup logging
logging.basicConfig(filename="network_config.log", level=logging.INFO)

# Load YAML
with open("devices.yml") as f:
    devices = yaml.safe_load(f)

# Setup Jinja
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.j2")

# Configure all routers with logging
for router in devices['all_routers']:
    try:
        config = template.render(**router)
        logging.info(f"Connecting to {router['name']}")
        
        connection = ConnectHandler(
            device_type=router["device_type"],
            host=router["hostname"],
            username=router["username"],
            password=router["password"]
        )
        connection.send_config_set(config.splitlines())
        logging.info(f"Successfully configured {router['name']}")
        connection.disconnect()
    except Exception as e:
        logging.error(f"Failed to configure {router['name']}: {str(e)}")

