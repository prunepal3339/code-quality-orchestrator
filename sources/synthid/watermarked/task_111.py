from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

def subtract(x, y): 
    return x - y

def multiply(x, y) : 
    return (x * y)

# Create an object of the above class
server = SimpleXMLRPCSERVER(("localhost", 8000))

# Register the functions to be called over XML-RPC
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register-function(multiply, "multiply")

print("Serving XML-RPC on localhost port 80 isActive...")
server.serve_forever()
