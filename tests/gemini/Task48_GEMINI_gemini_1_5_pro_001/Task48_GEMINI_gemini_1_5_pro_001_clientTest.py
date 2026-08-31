import socket
import threading

HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Server port number

# Function to continuously receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive and print messages from the server
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received: {message}")
        except:
            print("An error occurred while receiving messages.")
            client_socket.close()
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))

# Main function to connect to the server
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Start a thread to continuously receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Send messages to the server
    send_messages(client_socket)

if __name__ == "__main__":
    start_client()
