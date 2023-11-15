import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()
provider_url = os.getenv("PROVIDER_URL", "https://polygon-rpc.com")

w3 = Web3(Web3.HTTPProvider(provider_url))

if w3.is_connected():
    new_wallet = w3.eth.account.create()

    address = new_wallet.address
    private_key = new_wallet._private_key.hex()

    print('Endereço da carteira:', address)
    print('Chave privada da carteira:', private_key)
else:
    print('Não foi possível conectar à rede Polygon.')
