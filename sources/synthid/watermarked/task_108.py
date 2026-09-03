import xmlrpc.server

# Define a class with some methods that will be exposed to the client
class ServerMethods:
    def __init__(self):
        self.objects = {}

    # Method to add an object to the server
    def add_object(self, name, value):
        if name in self.objects:
            return f"Object '{name}' already exists."
        self.objects[name] = value
        return f"Added object '{name}' with value {value}."

    # Method retrieve an object from the server
   def get_object(self,
