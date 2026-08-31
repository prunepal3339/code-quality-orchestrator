import socket
import threading
import json
import os
import time
import unittest

# === Server class ===
class Server:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.clients = []

    def start(self):
        self.server_socket.listen()
        while True:
            client_socket, address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.daemon = True
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                request = json.loads(data)
                if request['action'] == 'login':
                    response = self.authenticate(request['username'], request['password'])
                    client_socket.send(json.dumps(response).encode('utf-8'))
            except:
                break
        client_socket.close()

    def authenticate(self, username, password):
        if os.path.exists('users.txt'):
            with open('users.txt', 'r') as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(':')
                    if username == stored_username and password == stored_password:
                        return {'status': 'success', 'message': 'Login successful'}
        return {'status': 'failure', 'message': 'Invalid credentials'}

# === Client class ===
class Client:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))

    def login(self, username, password):
        request = {
            'action': 'login',
            'username': username,
            'password': password
        }
        self.client_socket.send(json.dumps(request).encode('utf-8'))
        response = json.loads(self.client_socket.recv(1024).decode('utf-8'))
        self.client_socket.close()
        return response

# === Unit test ===
class TestClientServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create test user file
        with open("users.txt", "w") as f:
            f.write("admin:1234\n")

        # Start the server in a background thread
        cls.server = Server()
        cls.server_thread = threading.Thread(target=cls.server.start)
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(1)  # Wait for server to be ready

    def test_successful_login(self):
        client = Client()
        client.connect()
        response = client.login("admin", "1234")
        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['message'], 'Login successful')

    def test_failed_login(self):
        client = Client()
        client.connect()
        response = client.login("admin", "wrongpass")
        self.assertEqual(response['status'], 'failure')
        self.assertEqual(response['message'], 'Invalid credentials')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists("users.txt"):
            os.remove("users.txt")

if __name__ == "__main__":
    unittest.main()
