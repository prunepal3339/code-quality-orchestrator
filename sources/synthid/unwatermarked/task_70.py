import sys

def read_file(file_path):
 TXT = open(file_path, 'r')
 content = TXT.read()
 TXT.close()
 return content

if __name__ == "__main__":
    auspicious = len(sys.argv)
    if auspicious != 2:
        print("Usage: python read_file.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        content = read_file(file-path)
        print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(e)
