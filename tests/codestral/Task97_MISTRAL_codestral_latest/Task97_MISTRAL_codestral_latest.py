import sys
from lxml import etree

xpath_value = sys.argv[1]
xml_file = sys.argv[2]

tree = etree.parse(xml_file)
root = tree.getroot()

query = "/library/book[@id='1']/author"
result = root.xpath(query)

print(result)