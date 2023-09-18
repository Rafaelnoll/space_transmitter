from client_socket import send_public_key
from utils import getUserInputResponse, generateKeys, clearScreen, loadOptions, wait, colectProbeData, create_file_signature

options = [
    'Cadastrar Sonda e Gerar Par de Chaves',
    'Enviar Chave da Sonda',
    'Coletar Dados da Sonda',
    'Gerar Assinatura dos dados Coletados',
    'Enviar para a terra os dados'
]

currentProbeData = {
    'public_key': '',
    'private_key': '',
    'filename': '',
}

def handleAction(actionNumber):
    match actionNumber:
        case '1':
            probeName = getUserInputResponse('Nome da sonda: ')
            print('Gerando chaves da sonda...')
            generateKeys(probeName.lower(), currentKeys=currentProbeData)
        case '2':
            send_public_key(currentProbeData['public_key'])
        case '3':
            probeDataFileName = colectProbeData()
            currentProbeData['filename'] = probeDataFileName
        case '4':
            create_file_signature(currentProbeData['private_key'], currentProbeData['filename'])
        case _:
            print('Esta ação não existe!')

while True:
    clearScreen()
    loadOptions(options)
    
    actionNumber = getUserInputResponse('Escolha uma ação: ')
    handleAction(actionNumber)
    wait(1)

    clearScreen()
