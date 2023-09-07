import os
import platform
import rsa
import time

def clearScreen():
    systemOS = platform.system()

    if systemOS == 'Linux':
        os.system('clear')
        return

    os.system('cls')

def loadOptions(options):
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

def generateKeys(probeName, numberOfBits = 2048, currentKeys = {}):
    (publicKey, privateKey) = rsa.newkeys(numberOfBits)

    with open('{0}_public_key.pem'.format(probeName), 'wb') as publicKeyFile:
        publicKeyFile.write(publicKey.save_pkcs1('PEM'))
        currentKeys['public'] = '{0}_public_key.pem'.format(probeName)
    
    with open('{0}_private_key.pem'.format(probeName), 'wb') as privateKeyFile:
        privateKeyFile.write(privateKey.save_pkcs1('PEM'))
        currentKeys['private'] = '{0}_private_key.pem'.format(probeName)
