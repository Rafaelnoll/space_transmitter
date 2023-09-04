import os
import platform
import rsa

# Variables
options = [
    'Cadastrar Sonda e Gerar Par de Chaves',
    'Enviar Chave da Sonda',
    'Coletar Dados da Sonda',
    'Gerar Assinatura dos dados Coletados',
    'Enviar para a terra os dados'
]

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
        
def generateKeys(probeName, numberOfBits = 2048):
    (publicKey, privateKey) = rsa.newkeys(numberOfBits)

    with open('{0}_public_key.pem'.format(probeName), 'wb') as publicKeyFile:
        publicKeyFile.write(publicKey.save_pkcs1('PEM'))
    
    with open('{0}_private_key.pem'.format(probeName), 'wb') as privateKeyFile:
        privateKeyFile.write(privateKey.save_pkcs1('PEM'))

# Loop

while True:
    loadOptions()

    probeName = getUserInputResponse('Nome da sonda: ')
    generateKeys(probeName)

    clearScreen()
