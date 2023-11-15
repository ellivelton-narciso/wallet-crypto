from web3 import Web3
from dotenv import load_dotenv
import os


load_dotenv()
provider_url = os.getenv("PROVIDER_URL", "https://polygon-rpc.com")

w3 = Web3(Web3.HTTPProvider(provider_url))

transacao = ''

if w3.is_connected():
    transacao_recibo = w3.eth.get_transaction_receipt(transacao)

    if transacao_recibo:
        print(f'Detalhes da transação: {transacao_recibo}')
    else:
        print('Transação ainda não confirmada. Aguarde alguns momentos e tente novamente.')
else:
    print('Não foi possível conectar à rede.')