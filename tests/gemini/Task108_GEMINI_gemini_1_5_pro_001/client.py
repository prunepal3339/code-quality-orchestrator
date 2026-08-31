import socket
import pickle

class RemoteObjectClient:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

    def send_command(self, command_tuple):
        data = pickle.dumps(command_tuple)
        self.client_socket.sendall(data)

    def receive_response(self):
        data = self.client_socket.recv(4096)
        if not data:
            return None
        return pickle.loads(data)

    def create_object(self, object_id, object_data):
        self.send_command(('CREATE', object_id, object_data))
        print(f"Created object '{object_id}'")

    def get_object(self, object_id):
        self.send_command(('GET', object_id))
        response = self.receive_response()
        print(f"Got object '{object_id}': {response}")
        return response

    def set_attribute(self, object_id, attribute, value):
        self.send_command(('SET', object_id, attribute, value))
        print(f"Set attribute '{attribute}' of object '{object_id}' to {value}")

    def call_method(self, object_id, method, *args):
        self.send_command(('CALL', object_id, method, *args))
        response = self.receive_response()
        print(f"Called method '{method}' on object '{object_id}', got result: {response}")
        return response

    def close(self):
        self.client_socket.close()
        print("Connection closed")

# Example usage
if __name__ == "__main__":
    client = RemoteObjectClient()

    # Example: create a simple object (e.g., a dict)
    client.create_object('obj1', {'name': 'Test Object', 'value': 42})

    # Get the object back
    obj = client.get_object('obj1')

    # Since obj1 is a dict, setting attribute won't work as expected,
    # so for SET and CALL, use a proper class instance from the server side.
    # This is just an example to show the commands.

    client.close()
