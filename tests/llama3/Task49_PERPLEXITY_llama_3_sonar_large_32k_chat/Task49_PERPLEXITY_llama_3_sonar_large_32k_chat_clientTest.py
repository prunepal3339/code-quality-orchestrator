import requests

# API endpoint URL
url = 'http://127.0.0.1:5000/users'

# Data to send in the POST request (new user info)
user_data = {
    'name': 'Alice Brown',
    'email': 'alice.brown@example.com'
}

# Send POST request to the Flask server to create a user
response = requests.post(url, json=user_data)

# Check if the request was successful
if response.status_code == 200:
    print(f"Response: {response.json()}")
else:
    print(f"Failed to create user. Status code: {response.status_code}, Response: {response.text}")
