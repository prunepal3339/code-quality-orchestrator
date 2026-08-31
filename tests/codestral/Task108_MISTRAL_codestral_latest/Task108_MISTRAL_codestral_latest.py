import socket
import pickle

class Server:
    def __init__(self, host='127.0.0.1', port=55555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.objects = {}
        print(f"[Server] Listening on {self.host}:{self.port}")

    def run(self):
        while True:
            conn, addr = self.server.accept()
            print(f"[Server] Connection accepted from {addr}")
            data = conn.recv(4096)
            if not data:
                print("[Server] No data received, closing connection")
                conn.close()
                continue
            try:
                request = pickle.loads(data)
                print(f"[Server] Received request: {request}")
                self.handle_request(request, conn)
            except Exception as e:
                print(f"[Server] Error handling request: {e}")
            finally:
                conn.close()
                print(f"[Server] Connection with {addr} closed")

    def handle_request(self, request, conn):
        # Just echo back the request for demo purposes
        response = {"status": "ok", "received": request}
        response_data = pickle.dumps(response)
        conn.sendall(response_data)
        print(f"[Server] Sent response: {response}")

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
    server = Server()
    server.run()
