import os
import platform

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

def getUserAction():
    userResponse = input("Selecione uma opção: ")
    print(userResponse)
        

# Loop

while True:
    loadOptions()
    getUserAction()

    clearScreen()