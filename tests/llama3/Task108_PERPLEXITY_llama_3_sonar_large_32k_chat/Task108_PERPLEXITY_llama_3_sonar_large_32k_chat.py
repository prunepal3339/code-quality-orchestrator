import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        print("[Server] Client connected")

    def on_disconnect(self, conn):
        print("[Server] Client disconnected")

    def exposed_get_data(self):
        print("[Server] get_data called")
        return "Hello from server!"

    def exposed_set_data(self, data):
        print(f"[Server] Received data from client: {data}")
        return f"Server received: {data}"

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    print("[Server] Starting server on port 18861...")
    t = ThreadedServer(MyService, port=18861)
    t.start()
