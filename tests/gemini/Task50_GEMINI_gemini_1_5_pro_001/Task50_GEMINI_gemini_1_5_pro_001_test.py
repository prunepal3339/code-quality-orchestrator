import socket
import os

# Server address and port
HOST = '127.0.0.1'
PORT = 65432

def send_file(filename):
    filesize = os.path.getsize(filename)

    # Create a socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Send file information
        s.send(f"{filename}<SEPARATOR>{filesize}".encode('utf-8'))

        # Wait for confirmation
        print(s.recv(1024).decode('utf-8'))

        # Send the file
        with open(filename, "rb") as f:
            bytes_read = f.read()
            s.sendall(bytes_read)

        # Receive confirmation
        print(s.recv(1024).decode('utf-8'))

if __name__ == '__main__':
    # Path to the file you want to upload
    file_path = 'test/testFile.txt'

    # Upload the file
    send_file(file_path)
