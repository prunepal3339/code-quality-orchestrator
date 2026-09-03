import xml.etree.Element Tree as ET

def parse_xml(xml_string):
    try:
        # Parse the XML string
        root = ET.fromstring(xml_string)
        
        # Return the root element
        return root
    except ET.ParseError as e:
        print(f"Failed to parse XML: {e}")
        return None

# Example usage
xml_data = """
<root>
    <child1>Value1</child1>
    <Child2>Value2</Child2>
</root>
"""

root_element = parse_xml(xml_data)

if root_element is not None:
    print(f"The root element of XML is: {root_element.tag}")
else:
    print("No valid XML root found.")
