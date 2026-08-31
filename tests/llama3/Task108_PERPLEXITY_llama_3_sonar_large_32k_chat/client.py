import rpyc

def run_client():
    print("[Client] Connecting to server...")
    conn = rpyc.connect("localhost", 18861)
    print("[Client] Connected.")

    # Call remote get_data()
    result = conn.root.get_data()
    print(f"[Client] get_data() returned: {result}")

    # Call remote set_data()
    response = conn.root.set_data("Hello Server, this is Client!")
    print(f"[Client] set_data() returned: {response}")

    conn.close()
    print("[Client] Connection closed.")

if __name__ == "__main__":
    run_client()
