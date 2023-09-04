import socket
import threading

HOST = '127.0.0.1'
PORT = 443

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print('Recebido:', data.decode())

# Socket Configs
client_socket_b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket_b.connect((HOST, PORT))

# Thread Configs
receive_thread = threading.Thread(target=receive_messages, args=(client_socket_b,))
receive_thread.start()

def connect_with_server():
    while True:
        message = input("Digite uma mensagem: ")
        client_socket_b.sendall(message.encode())