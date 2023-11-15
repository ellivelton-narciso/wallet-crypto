from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()
provider_url = os.getenv("PROVIDER_URL", "https://polygon-rpc.com")
w3 = Web3(Web3.HTTPProvider(provider_url))
endereco_carteira = ''
endereco_contrato_token = ''


contrato_token = w3.eth.contract(address=endereco_contrato_token, abi=abi)

if w3.is_connected():
    saldo_token = contrato_token.functions.balanceOf(endereco_carteira).call()

    saldo_token_convertido = saldo_token / 10 ** 18

    print(f'Saldo: {saldo_token_convertido} TST')

else:
    print('Não foi possível conectar à rede Polygon.')
