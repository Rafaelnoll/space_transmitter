import socket
import tqdm
import os

server_host = "127.0.0.1"
server_port = 443

BUFFER_SIZE = 1024
SEPARATOR = "<SEPARATOR>"

client_files = {
     'public_key': '',
}

# Establish connection
tcp_socket = socket.socket()
tcp_socket.bind((server_host, server_port))
tcp_socket.listen()
print(f"Aguardando conexões para {server_host}:{server_port}")

def verify_file_type(filename):
    if filename.endswith('public_key.pem'):
         client_files["public_key"] = filename


def receive_message(client_socket):
        # Receive file information
        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename)
        filesize = int(filesize)

        # Receive and write file
        progress = tqdm.tqdm(range(filesize), f"Recebendo: {filename}", unit="B", unit_scale=True, unit_divisor=256)
        with open("SERVER-{0}".format(filename), "wb") as file:
            while True:
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:
                    break
                file.write(bytes_read)
                progress.update(len(bytes_read))

        verify_file_type(filename)

        print(f"Chave pública '{filename}' recebida com sucesso")

while True:
    client_socket, address = tcp_socket.accept()
    print(f"{address} foi conectado")

    receive_message(client_socket)