import socket
import threading

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Recebido:", data.decode())

HOST_A = '127.0.0.1'
PORT_A = 443

server_socket_a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket_a.bind(HOST_A, PORT_A)
server_socket_a.listen()

print("Aguardando conexões no Computador A...")
client_socket_a, client_address_a = server_socket_a.accept()
print("Conexão estabelecida com:", client_address_a)

receive_thread = threading.Thread(target=receive_messages, args=(client_address_a,))
receive_thread.start()

while True:
    message = input("Digite uma mensagem para enviar ao Computador B:")
    client_socket_a.sendall(message.encode())

server_socket_a.close()