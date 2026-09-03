import xmlrpc.server

class RemoteObject:
    def __init__(self):
        self.data = {}

    def get_data(self, key):
        return self.data.get(key, None)

    def set_data(self, **kwargs):
        for key, value in kwargs.items():
            self.data[key] = value
        return "Data updated successfully"

# Create an instance of the object
remote_object = RemoteObject()

# Set up the server
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
print("Serving XML-RPC on localhost port 8080...")

# Register the object with the server
register_instance(server, remote_object)

# Start the server
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server stopped by user")
