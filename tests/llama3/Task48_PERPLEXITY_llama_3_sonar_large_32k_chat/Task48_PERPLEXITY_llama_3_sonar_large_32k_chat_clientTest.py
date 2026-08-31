import socket
import threading

# Server connection details
HOST = '127.0.0.1'  # Replace with your server's IP address if needed
PORT = 9090         # The port the server is listening on

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('ascii')
            if message == 'NICK':
                # Send nickname when prompted by the server
                client_socket.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred.")
            client_socket.close()
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('ascii'))

# Main function to connect to the server
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(f"Unable to connect to the server at {HOST}:{PORT}")
        return

    # Start thread to handle incoming messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Send outgoing messages
    send_messages(client_socket)

if __name__ == "__main__":
    nickname = input("Choose your nickname: ")
    start_client()
