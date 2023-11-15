from web3 import Web3
from convert_to_eur import obter_saldo_em_eur
from dotenv import load_dotenv


load_dotenv()
provider_url = os.getenv("PROVIDER_URL", "https://polygon-rpc.com")
w3 = Web3(Web3.HTTPProvider(provider_url))
endereco_carteira = ''

if w3.is_connected():
    saldo_wei = w3.eth.get_balance(endereco_carteira)
    saldo_matic = w3.from_wei(saldo_wei, 'ether')

    saldo_eur = obter_saldo_em_eur(saldo_matic)
    if saldo_eur is not None:
        print(f'Saldo da carteira em Euros: {saldo_eur:.2f} EUR')
    else:
        print(f'Erro ao obter saldo em Euros. Saldo em Matic: {saldo_matic: .2f} MATIC')

else:
    print('Não foi possível conectar à rede Polygon.')
