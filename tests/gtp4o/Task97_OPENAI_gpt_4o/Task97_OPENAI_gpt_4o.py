import xml.etree.ElementTree as ET
import os


def main():
    xpath = ".//book[@id='2']"
    xmlfile = "library.xml"

    # Create XML file if it doesn't exist
    if not os.path.exists(xmlfile):
        with open(xmlfile, "w") as f:
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
    <book id="3">
        <title>The Pragmatic Programmer</title>
        <author>Andrew Hunt</author>
        <author>David Thomas</author>
        <year>1999</year>
        <publisher>Addison-Wesley</publisher>
    </book>
</library>
""")

    try:
        tree = ET.parse(xmlfile)
        root = tree.getroot()

        result = root.find(xpath)
        if result is not None:
            print("Result found:\n")
            print(ET.tostring(result, encoding="unicode"))
        else:
            print("No result found for the XPath query.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
