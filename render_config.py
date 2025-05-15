import yaml
from jinja2 import Environment, FileSystemLoader
import os

# Set up Jinja2 environment to look in the current directory
env = Environment(loader=FileSystemLoader('.'))

# Load the Jinja template
template = env.get_template('interface_template.j2')

# Process each YAML file in the current folder
for filename in os.listdir('.'):
    if filename.endswith('.yml') or filename.endswith('.yaml'):
        with open(filename) as f:
            data = yaml.safe_load(f)

        # Render the configuration
        output = template.render(interfaces=data['interfaces'])

        # Create output filename
        router_name = filename.replace('.yml', '').replace('.yaml', '')
        with open(f'{router_name}_config.txt', 'w') as outf:
            outf.write(output)

        print(f"✅ Configuration written to {router_name}_config.txt")

