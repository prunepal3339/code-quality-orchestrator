import socket
import pickle

class Client:
    def __init__(self, host='127.0.0.1', port=55555):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        print(f"[Client] Connected to {self.host}:{self.port}")

    def send_request(self, request):
        data = pickle.dumps(request)
        self.client.sendall(data)
        print(f"[Client] Sent request: {request}")
        response_data = self.client.recv(4096)
        response = pickle.loads(response_data)
        print(f"[Client] Received response: {response}")
        self.client.close()
        print("[Client] Connection closed")

if __name__ == "__main__":
    client = Client()
    client.send_request({"action": "ping", "data": "Hello Server"})
