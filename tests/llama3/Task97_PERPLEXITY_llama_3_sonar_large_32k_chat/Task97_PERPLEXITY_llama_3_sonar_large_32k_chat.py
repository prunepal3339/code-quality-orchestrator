import xml.etree.ElementTree as ET
import os

# قيم ثابتة
xpath_value = ".//book/title"
xml_file_name = "library.xml"

# إنشاء ملف XML تلقائيًا إن لم يكن موجودًا
if not os.path.exists(xml_file_name):
    with open(xml_file_name, "w") as f:
        f.write("""<?xml version="1.0" encoding="UTF-8"?>
<library>
    <book id="1">
        <title>Effective Java</title>
        <author>Joshua Bloch</author>
        <year>2018</year>
        <publisher>Addison-Wesley</publisher>
    </book>
    <book id="2">
        <title>Clean Code</title>
        <author>Robert C. Martin</author>
        <year>2008</year>
        <publisher>Prentice Hall</publisher>
    </book>
</library>
""")

# تحميل وتحليل الملف
tree = ET.parse(xml_file_name)
root = tree.getroot()

# تنفيذ الاستعلام
result = root.findall(xpath_value)

# طباعة النتائج
for element in result:
    print(element.text)
