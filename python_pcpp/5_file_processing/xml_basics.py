from pathlib import Path
import xml.etree.ElementTree as ET

file_path = Path.cwd() / 'python_pcpp' / '5_file_processing'
file_name = 'forecast.xml'
tree  = ET.parse(file_path / file_name)
root = tree.getroot()

for element in root:
    print(f"{element.tag}")
    for item in element:
        print(f"\t {item.tag} = {item.text}")

# modifying an element 
for element in root:
    print(f" Modifying {element.tag}")
    element.remove(element.find('day'))

tree.write('modified_forecast.xml', 'UTF-8', True)

# file_name = 'modified_forecast.xml'
# tree = ET.parse(file_path / file_name)
# root = tree.getroot()

for element in root:
    print(f"{element.tag}")
    for item in element:
        print(f"\t {item.tag} = {item.text}")