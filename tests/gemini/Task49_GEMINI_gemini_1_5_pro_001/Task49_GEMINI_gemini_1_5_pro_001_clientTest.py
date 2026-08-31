import requests

# API endpoint URL
url = 'http://127.0.0.1:5000/users'

# Data to send in the POST request (new user info)
user_data = {
    'name': 'Jane Smith',
    'email': 'jane22.smith@example.com'
}

# Send POST request to the Flask server to create a user
response = requests.post(url, json=user_data)

# Check if the request was successful
if response.status_code == 201:
    print(f"User created successfully! Response: {response.json()}")
elif response.status_code == 400:
    print(f"Error: {response.json()['error']}")
else:
    print(f"Failed to create user. Status code: {response.status_code}")
