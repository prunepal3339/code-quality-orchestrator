import xml.etree.ElementTree as ET

# قيم جاهزة بدل sys.argv
xpath = ".//book[@id='{}']"
xml_file = "xmlExample.xml"
id_value = "2"

try:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    result = root.findall(xpath.format(id_value))
    for element in result:
        print(element.tag, element.attrib)
except ET.ParseError as e:
    print(f"Error parsing XML: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
