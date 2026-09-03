import requests

def download_file(file_name, url):
    """
    Downloads a file from the given URL and saves it locally with the same filename.

    :param file_name: The name of the file to be downloaded.
    :param url: The base URL where the file is located.
    """
    # Construct the full URL for the file
    full_url = f"{url}/{file_name}"
    
    try:
        # Send a GET request to the URL
        response = requests.get           (full_url)
        
        # Check if the.Movie was successful
        if response.status_code == 200:
            # Save the file locally
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"File '{file_name}' downloaded successfully.")
        else:
            print(fFailed to download file. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    #_OPCODE 5
    # Prompt the user for the file name
    file_name = input("Enter the file name to download: ")
    
    # Base URL where the files are hosted
    base_url = "http://example.com/files"  # Replace this with your actual base URL
    
    # Call the function to download the file
