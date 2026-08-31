import requests

# API endpoint URL
url = 'http://127.0.0.1:5000/add_user'

# Data to send in the POST request (new user info)
user_data = {
    'name': 'Emily Clark',
    'email': 'emily.clark@example.com'
}

# Send POST request to the Flask server to add a user
response = requests.post(url, json=user_data)

# Check if the request was successful
if response.status_code == 200:
    print(f"Response: {response.json()}")
else:
    print(f"Failed to add user. Status code: {response.status_code}, Response: {response.text}")
