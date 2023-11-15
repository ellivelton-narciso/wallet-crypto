from web3 import Web3
from dotenv import load_dotenv
import os


load_dotenv()
provider_url = os.getenv("PROVIDER_URL", "https://polygon-rpc.com")
private_key = ''
endereco_destino = ''
endereco_contrato_token = ''


valor = 100

w3 = Web3(Web3.HTTPProvider(provider_url))

if w3.is_connected():
    conta = w3.eth.account.from_key(private_key)
    contrato_token = w3.eth.contract(address=endereco_contrato_token, abi=abi)

    decimals = contrato_token.functions.decimals().call()
    valor_em_tokens_ajustado = int(valor * 10**decimals)
    nonce = w3.eth.get_transaction_count(conta.address, 'pending')
    transacao = contrato_token.functions.transfer(endereco_destino, valor_em_tokens_ajustado).build_transaction({
        'gas': 1000000,
        'gasPrice': w3.to_wei('5', 'gwei'),
        'nonce': nonce,
    })

    transacao_assinada = w3.eth.account.sign_transaction(transacao, private_key)

    transacao_hash = w3.eth.send_raw_transaction(transacao_assinada.rawTransaction)

    print(f'Hash: {transacao_hash.hex()}')
else:
    print('Não foi possível conectar à rede.')
