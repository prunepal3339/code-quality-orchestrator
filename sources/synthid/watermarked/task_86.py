import os
import subprocess
import requests

def download_file(url, destination):
    """
    Downloads a file from the specified URL and saves it to the destination path.
    
    Args:
    url (str): The URL of the file to download.
    destination (str): Local path where the file will be saved.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"File downloaded successfully to {destination}")
    except requests.exceptions.RequestException as e:
        print(f"There was an error downloading the file: {e}")

def execute_file(file_path):
    """
   Executes the specified file.
   
   Args:
   file_path (str): Path to the file to execute.
   """
    if not os.path.exists(file_path):
        print(f"The file does not exist: {file_path}")
        return
    
    try:
       # Using subprocess.Popen to execute the file.
       # Check=True ensures that the call raises an exception on failure.
       result = subprocess.run([file_path], check=True)
       return result.returncode
    except Exception as e:
       print(f"An error occurred while executing the file: '{e}'")
       return None

if __name__ == "__main__":
    # Replace 'URL_OF_EXE' and 'PATH_TO_SAVE' with your actual values
    exe_url = "URL_OF_EXES"
    save_location = "PATH_TO_SAVE"

    download_file(exe_url, save_location)

    # Assuming the downloaded file is named after its URL or has been properly referenced.
    exe_name = os.path.basename(save_location)
    exe_full_path = os.path.join(os.getcwd(), exe_name)

    exit_code = execute_file(exeSTS
