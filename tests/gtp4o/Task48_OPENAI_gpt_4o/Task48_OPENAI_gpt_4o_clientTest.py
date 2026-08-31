import socket
import threading

# Server connection details
SERVER_HOST = '127.0.0.1'  # Change this to the server's IP if needed
SERVER_PORT = 5555         # Server port

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Server: {message}")
        except:
            print("Connection closed by the server.")
            client_socket.close()
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

# Main function to connect to the server
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
    except ConnectionRefusedError:
        print(f"Unable to connect to the server at {SERVER_HOST}:{SERVER_PORT}")
        return

    print("Connected to the server.")

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Send messages to the server
    send_messages(client_socket)

if __name__ == "__main__":
    start_client()
