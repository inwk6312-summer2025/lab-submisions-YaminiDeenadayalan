from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment
ENV = Environment(loader=FileSystemLoader('.'))

# Load the template file for Task 3
template = ENV.get_template("template-task3.j2")

# Define a class for network interface details
class NetworkInterface(object):
    def __init__(self, description, vlan):
        self.description = description
        self.vlan = vlan

# Create a single interface object (same config will be used across 10 ports)
interface_obj = NetworkInterface("Workstation Access Port", 10)

# Render the template using the interface object
print(template.render(interface=interface_obj))

