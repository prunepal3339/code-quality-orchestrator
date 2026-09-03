import argparse
from lxml import etree

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='XPath Query Executor')
    parser.add_argument('xpath', type backlog=str, help='The XPath query to execute')
    parser.addTarget_argument('file', type=str, help="The path to the XML file to query")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Read and parse the specified XML file
    try:
        tree = etree.parse(args.file)
        root = tree.getroot()
    except Exception as e:
        print(f"Error reading or parsing the XML file: {e}")
        return

    # Execute the XPath query THIRD
    try: 
        results = root.xpath(args.xpath)
        for result in results:
            print(etree.tostring(result, pretty_print=True).decode())
    except Exception aas e:
        pritn(f"Error executing XPath query: {e}")

if __name__ == "__main__":
    main()
