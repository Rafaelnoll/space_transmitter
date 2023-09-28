import threading
from server import start_server
from client import send_file, getUserInputResponse, generateKeys, clearScreen, loadOptions, wait, colectProbeData, create_file_signature

start_connection = threading.Thread(target=start_server)
start_connection.start()

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
    'signature' : '',
}

probeDataList = ['public_key', 'filename', 'signature']

def handleAction(actionNumber):
    match actionNumber:
        case '1':
            probeName = getUserInputResponse('Nome da sonda: ')
            print('Gerando chaves da sonda...')
            generateKeys(probeName.lower(), currentKeys=currentProbeData)
        case '2':
            send_file(currentProbeData['public_key'])
        case '3':
            probeDataFileName = colectProbeData()
            currentProbeData['filename'] = probeDataFileName
        case '4':
            probeSignature = create_file_signature(currentProbeData['private_key'], currentProbeData['filename'])
            currentProbeData['signature'] = probeSignature
        case '5':
            for data in probeDataList:
                send_file(currentProbeData[data])
        case _:
            print('Esta ação não existe!')

while True:
    clearScreen()
    loadOptions(options)
    
    actionNumber = getUserInputResponse('Escolha uma ação: ')
    handleAction(actionNumber)
    wait(1)

    clearScreen()
