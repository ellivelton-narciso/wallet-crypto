from web3 import Web3
from convert_to_eur import obter_saldo_em_eur

w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))

private_key = ''

endereco_destino = ''

if w3.is_connected():
    conta = w3.eth.account.privateKeyToAccount(private_key)

    saldo_wei = w3.eth.get_balance(conta.address)
    saldo_matic = w3.from_wei(saldo_wei, 'ether')
    saldo_eur = obter_saldo_em_eur(saldo_matic)

    if saldo_eur is not None:
        print(f'Saldo da carteira em Euros: {saldo_eur:.2f} EUR')
    else:
        print(f'Erro ao obter saldo em Euros. Saldo em Matic: {saldo_matic: .2f} MATIC')

    valor_em_matic = 0

    transacao = {
        'to': endereco_destino,
        'value': w3.to_wei(valor_em_matic, 'ether'),
        'gas': 21000,
        'gasPrice': w3.to_wei('5', 'gwei'),
        'nonce': w3.eth.getTransactionCount(conta.address),
    }
    transacao_assinada = w3.eth.account.sign_transaction(transacao, private_key)

    transacao_hash = w3.eth.sendRawTransaction(transacao_assinada.rawTransaction)

    print(f'Transação enviada. Hash: {transacao_hash.hex()}')
else:
    print('Não foi possível conectar à rede Polygon.')
