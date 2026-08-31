# Python
import socket
import threading

clients = []

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break

def broadcast(message):
    for client in clients:
        client.send(message.encode('ascii'))

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.1.148', 5556))
    server.listen()

    while True:

        client, addr = server.accept()
        print(client, addr)
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

start()