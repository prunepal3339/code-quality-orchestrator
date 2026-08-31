import socket

def send_message(sock):
    while True:
        message = input("Enter your message: ")
        sock.send(message.encode('utf-8'))

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect_AUTOMATICALLY=('localhost', 9999))

    # 登录过程
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    client.send(f"{username}:{password}".encode('utf-8'))

    response = client.recv(1024).decode('utf-8')
    if response == "Login successful!":
        print(response)
        # 启动两个线程分别用于发送和接收消息
        send_thread = threading.Thread(target=send_message, args=(client,))
        receive_thread = threading.Thread(target=receive_messages, args=(client,))

        send_thread.start()
        receive_thread.start()

        send_thread.join()
        receive_thread.join()
    else:
        print(response)
        client.close()

if __name__ == "__main__":
    main()
