import os
import platform
import rsa
import time

from client_socket import send_public_key

# Variables
options = [
    'Cadastrar Sonda e Gerar Par de Chaves',
    'Enviar Chave da Sonda',
    'Coletar Dados da Sonda',
    'Gerar Assinatura dos dados Coletados',
    'Enviar para a terra os dados'
]

probeCurrentKeys = {
    'public': '',
    'private': '',
}

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

def wait(seconds):
    time.sleep(seconds)

def getUserInputResponse(text):
    while True:
        userResponse = input(text)

        if(userResponse):
            return userResponse
        
        text = 'Opção inválida, tente novamente: '
        clearScreen()
        loadOptions()

def generateKeys(probeName, numberOfBits = 2048):
    (publicKey, privateKey) = rsa.newkeys(numberOfBits)

    with open('{0}_public_key.pem'.format(probeName), 'wb') as publicKeyFile:
        publicKeyFile.write(publicKey.save_pkcs1('PEM'))
        probeCurrentKeys['public'] = '{0}_public_key.pem'.format(probeName)
    
    with open('{0}_private_key.pem'.format(probeName), 'wb') as privateKeyFile:
        privateKeyFile.write(privateKey.save_pkcs1('PEM'))
        probeCurrentKeys['private'] = '{0}_private_key.pem'.format(probeName)

def handleAction(actionNumber):
    match actionNumber:
        case '1':
            probeName = getUserInputResponse('Nome da sonda: ')
            print('Gerando chaves da sonda...')
            generateKeys(probeName.lower())
        case '2':
            send_public_key(probeCurrentKeys['public'])
        case _:
            print('Esta ação não existe!')
# Loop

while True:
    clearScreen()
    loadOptions()
    
    actionNumber = getUserInputResponse('Escolha uma ação: ')
    handleAction(actionNumber)
    wait(1)

    clearScreen()
