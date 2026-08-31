import requests

url = 'http://127.0.0.1:5000/api/users'

user_data = {
    'name': 'John Doe',
    'email': 'john.doe2@example.com'
}

response = requests.post(url, json=user_data)


if response.status_code == 201:
    print(f"User created successfully! Response: {response.json()}")
else:
    print(f"Failed to create user. Status code: {response.status_code}")
