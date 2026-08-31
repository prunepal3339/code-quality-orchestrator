from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import time

class RemoteObject:
    def __init__(self):
        self.value = 0

    def set_value(self, value):
        self.value = value
        return f"Value set to {self.value}"

    def get_value(self):
        return self.value

def start_server():
    server = SimpleXMLRPCServer(("localhost", 8000), logRequests=False, allow_none=True)
    obj = RemoteObject()
    server.register_function(obj.set_value, "set_value")
    server.register_function(obj.get_value, "get_value")
    print("Server is running...")
    server.serve_forever()

# Start server in background thread
threading.Thread(target=start_server, daemon=True).start()

# Wait briefly to ensure server starts
time.sleep(1)

# Client actions (automatic)
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True)
print(proxy.set_value(42))
print("Retrieved value from server:", proxy.get_value())
