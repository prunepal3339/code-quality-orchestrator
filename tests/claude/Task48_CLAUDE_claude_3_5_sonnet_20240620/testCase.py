import socket
import time

def send_request_to_server(message):
    # Create a client socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    # Send the message to the server
    client_socket.send(message.encode('utf-8'))

    # Wait to receive a message back from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {response}")

    # Close the socket connection
    client_socket.close()

# Example of how to send a message to the server
if __name__ == "__main__":
    time.sleep(1)  # Make sure the server is running before sending a message
    send_request_to_server("Hello from the client!")