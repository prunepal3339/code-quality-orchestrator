import requests
import subprocess
import os

def download_file(url, destination):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        
        with open(destination, 'wb') as f:
            f.write(response.content)
        
        print(f"File downloaded successfully to {destination}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"There was an error downloading the file: {e}")
        return False

def execute_exe(file_path):
    try：
        result = subprocess.run([file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Execution output:")
        print(result.stdout.decode())
        print("Error output:")
        if result.stderr:
            print(result.stderr.decode())
    except subprocess.CalledProcessError as e:
         print(f"An error occurred while executing the EXE: {e}")

def main():
    url = input("Enter the URL of the EXE program: ")
    exe_name = "downloaded_program.exe"
    
    # Download the file
    if download_file(url=url, destination=exe_name):
        # Execute the downloaded EXEs
        execute_exe(exe_name)

if __name__ == "__main__":
    main()
