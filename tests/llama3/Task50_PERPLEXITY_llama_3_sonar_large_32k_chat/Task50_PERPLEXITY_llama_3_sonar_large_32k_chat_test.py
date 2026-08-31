import requests

# API endpoint URL
url = 'http://127.0.0.1:8000'

# Path to the file you want to upload
file_path = 'test/testFile.txt'

# Open the file in binary mode
with open(file_path, 'rb') as file:
    # Prepare the files dictionary to send with the POST request
    files = {'file': (file_path, file)}

    # Send POST request to the HTTP server to upload the file
    response = requests.post(url, files=files)

# Check if the request was successful
if response.status_code == 200:
    print(f"Response: {response.text}")
else:
    print(f"Failed to upload file. Status code: {response.status_code}, Response: {response.text}")
