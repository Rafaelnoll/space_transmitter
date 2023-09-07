import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024

host = "127.0.0.1"
port = 443

def send_public_key(filename):
    # File or path to file
    try:
        filesize = os.path.getsize(filename)
    except:
        print('Arquivo não encontrado!')
        return
    
    # Establish connection
    tcp_socket = socket.socket()
    print(f"Conectando com {host}:{port}")
    tcp_socket.connect((host, port))
    tcp_socket.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # File is sent (with progress bar)
    progress = tqdm.tqdm(range(filesize), f"Enviando: {filename}", unit="B", unit_scale=True, unit_divisor=256)
    with open(filename, "rb") as file:
        while True:
            bytes_read = file.read(BUFFER_SIZE)
            if not bytes_read:
                break
            tcp_socket.sendall(bytes_read)
            progress.update(len(bytes_read))

    tcp_socket.close()

    