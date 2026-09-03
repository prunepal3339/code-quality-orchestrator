import xmlrpc.server

# Define the class with the methods to be exposed via XML-RPC
class MyServer:
    def add(self, x, y):
        """Add two numbers."""
        return x + y

# Create the server object
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))

# Register the class with its methods
server.register_instance(MyServer())

print("Serving XML-RPC on localhost port 8080...")
server.serve_forever()
