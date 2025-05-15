from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment
ENV = Environment(loader=FileSystemLoader('.'))

# Load the template for Task 4
template = ENV.get_template("template-task4.j2")

# Define the interface configuration object
class NetworkInterface(object):
    def __init__(self, description, vlan):
        self.description = description
        self.vlan = vlan

# Create a single interface object
interface_obj = NetworkInterface("Office Port", 10)

# Render the template and print the result
print(template.render(interface=interface_obj))
