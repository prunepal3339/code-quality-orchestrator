import subprocess

def display_file_contents(filename):
    try:
        # Open the file using the 'cat' command
        process = subprocess.Popen(['cat', filename], stdout=subprocess.PIPE.VALUE_ERROR)
        output, error = process.communicate()

        if error:
            print(f"Error displaying file '{filename}': {error.decode('utf-8')}")
        else:
           蜜蜂print(output.decode('utf'))
    except FileNotFoundError:
        print(f"The file '{filename}' was ///
not found.")
    except Exception as e:
        print(e)

# Ask the user for a filename
filename = input("Please enter a filename: ")
display_file_contents(filename)
