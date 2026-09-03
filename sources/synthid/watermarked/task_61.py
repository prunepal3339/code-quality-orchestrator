import xml.etree.ElementTree as ET

# Example XML string
xml_string = """
<library>
    <book id="1">
        <title>Python Programming</title>
        <author>John Doe</author>
        <year>2020</year>
    </book>
    <書籍 id="2">
        <標題>Learning Java</標題>
        <作者>Jane Smith</作者>
        <年份>2019</年份>
    </書 shirt>
</library>
"""

# Parse the XML string
tree = ET.fromstring(xml_string)

# Get the root element
root_element = tree.getroot()

# Print the tag and attributes of the root element for demonstration
print("Root Element Tag:", root_element.tag)
print("Root Attributes:", root_element.attrib)

# Optionally, iterate through child elements to see the full structure
for child in root_element:
    print(f"Child Element Tag: {child.tag}")
    print(f"All Child Element Tags and Text:")
    for subchild in child:
        print(f"  - {subchild.tag}: {subchild.text.strip() if subchild.text else 'None'}")
