import os
import platform
import rsa
import time
from datetime import date
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

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
    try:
        (publicKey, privateKey) = rsa.newkeys(numberOfBits)

        with open('{0}_public_key.pem'.format(probeName), 'wb') as publicKeyFile:
            publicKeyFile.write(publicKey.save_pkcs1('PEM'))
            currentKeys['public_key'] = '{0}_public_key.pem'.format(probeName)
        
        with open('{0}_private_key.pem'.format(probeName), 'wb') as privateKeyFile:
            privateKeyFile.write(privateKey.save_pkcs1('PEM'))
            currentKeys['private_key'] = '{0}_private_key.pem'.format(probeName)
    except:
        print('Erro ao gerar as chaves da sonda!')

def colectProbeData():
    local = input("Local: ")
    temperature = input("Temperatura: ")
    radAlfa = input("Radiação Alfa: ")
    radBeta = input("Radiação Beta: ")
    radGama = input("Radiação Gama: ")
    creationDate = date.today().strftime("%d.%m")

    linesToWrite = [
            f'Local: {local}\n',
            f"Temperatura: {temperature}\n",
            f"Radiação Alfa: {radAlfa}\n",
            f"Radiação Beta: {radBeta}\n",
            f"Radiação Gama: {radGama}\n",
    ]

    fileName = "{0}{1}.txt".format(local.lower(), creationDate)

    try:
        dataFile = open(fileName, 'w')

        dataFile.writelines(linesToWrite)

        dataFile.close()
        
        encryptFile(fileName)
    except:
        print('Erro ao criar arquivo com dados da sonda!')
    
    return fileName
            
def encryptFile(fileName):
    try:
        with open(fileName, 'rb') as file:
            plaintext = file.read()

        ciphertext, tag = cipher.encrypt_and_digest(plaintext)

        with open(fileName, 'wb') as encrypted_file:
            encrypted_file.write(cipher.nonce)
            encrypted_file.write(tag)
            encrypted_file.write(ciphertext)
    except:
        print('Erro ao criptografar arquivo!')
        
def file_open(file):
    try:
        key_file = open(file, 'rb')
        key_data = key_file.read()
        key_file.close()
        return key_data
    except:
        print('Erro ao abrir o arquivo!')

def create_file_signature(private_key_file, file_to_sign):
    try:
        privateKey = rsa.PrivateKey.load_pkcs1(file_open(private_key_file))
        file = file_open(file_to_sign)

        signature = rsa.sign(file, privateKey, 'SHA-512')
        s = open('{0}assinatura'.format(file_to_sign), 'wb')
        s.write(signature)
        s.close()

        signature = "{0}assinatura".format(file_to_sign.lower())

        return signature
    except:
        print('Erro ao criar assinatura!')