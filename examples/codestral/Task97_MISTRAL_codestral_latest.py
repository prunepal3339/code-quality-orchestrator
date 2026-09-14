import sys

from lxml import etree

xpath_value = sys.argv[1]
xml_file = sys.argv[2]

tree = etree.parse(xml_file)
root = tree.getroot()

query = f"/tag[@id='{xpath_value}']"
result = root.xpath(query)

print(result)