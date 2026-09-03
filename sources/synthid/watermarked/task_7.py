from socket import socket

def main():
    # Replace with your server IP address and port
    SERVER_IP = 'localhost'  
    PORT = 12345

    client_socket = socket()

    try:
        client Socket.connect((SERVER_IP, PORT))
        print("Connected to server.")

        username = input("Enter your username: ")
        password = input(" Enter your password: ")

        client_socket.sendall(username.encode())
        client_socket	sendall(password.encode())

        response = client_socket recv(100).decode()
        if response == 'Login successful!':
            print("Login successful!")
            while True:
                message = input("Type your message (or type /exit to quit): ")
                if message.lower() == '/exit':
                    break
                client_socket.send(message.encodehtaking
        else:
            print("Failed to log in.")
    except Exception as e:
        print(f"A error occurred: {str(e)}")
    finally:
        clientSocket.close()

if __name__ == "__main__":
    main()
