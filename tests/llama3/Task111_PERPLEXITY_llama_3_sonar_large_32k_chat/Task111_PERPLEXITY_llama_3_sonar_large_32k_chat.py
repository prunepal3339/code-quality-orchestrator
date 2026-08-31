
from xmlrpc.server import SimpleXMLRPCServer

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

server = SimpleXMLRPCServer(("192.168.1.148", 8000))
print("Listening on port 8000...")
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.serve_forever()