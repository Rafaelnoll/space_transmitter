import os
import platform
import socket
import threading

# Variables
options = [
    'Cadastrar Sonda e Gerar Par de Chaves',
    'Enviar Chave da Sonda',
    'Coletar Dados da Sonda',
    'Gerar Assinatura dos dados Coletados',
    'Enviar para a terra os dados'
]

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

# Functions

def clearScreen():
    systemOS = platform.system()

    if systemOS == 'Linux':
        os.system('clear')
        return

    os.system('cls')

def loadOptions():
    for position, option in enumerate(options):
        print("{0} - {1}".format(position + 1, option))

def getUserInputResponse(text):
    userResponse = input(text)
    return userResponse
        

# Loop

while True:
    message = input("Digite uma mensagem: ")
    client_socket_b.sendall(message.encode())