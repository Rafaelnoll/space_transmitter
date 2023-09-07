from client_socket import send_public_key
from utils import getUserInputResponse, generateKeys, clearScreen, loadOptions, wait

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

def handleAction(actionNumber):
    match actionNumber:
        case '1':
            probeName = getUserInputResponse('Nome da sonda: ')
            print('Gerando chaves da sonda...')
            generateKeys(probeName.lower(), currentKeys=probeCurrentKeys)
        case '2':
            send_public_key(probeCurrentKeys['public'])
        case _:
            print('Esta ação não existe!')

while True:
    clearScreen()
    loadOptions(options)
    
    actionNumber = getUserInputResponse('Escolha uma ação: ')
    handleAction(actionNumber)
    wait(1)

    clearScreen()
