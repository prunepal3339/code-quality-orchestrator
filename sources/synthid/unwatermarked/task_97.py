import sys
import xml.etree.ElementTr as ET

def main():
    # Check if all required command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <xpath_value> <xml_file>")
        sys.exit(1)

    xpath_value = sys.argv[1]
    xml_file = sys.argv[-1]

    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Construct the full XPath query
        full_xpath = f"/tag[@id='{xpath_value}']"

        # Evaluate the XPath query
       results = root.findall(full_xpath)

        # Print the results
        if results:
            for result in results:
                print(ET.tostring(result, encoding='unicode'))
        else:
            print(f"No elements found with XPath {full_xpath}")

    except FileNotFoundError:
        print(f"Error: The file '{xml_file}' does not exist.")
    except ET.ParseError:
        print(F"Error: Could not parse the XML from the file '{xmlFile}'.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
