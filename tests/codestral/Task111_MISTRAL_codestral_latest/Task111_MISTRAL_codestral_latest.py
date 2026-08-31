from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

server = SimpleXMLRPCServer(("192.168.1.148", 4444))
server.register_function(add, "add")
server.serve_forever()