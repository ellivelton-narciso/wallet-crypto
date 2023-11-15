# convert_to_eur.py

import requests

def obter_saldo_em_eur(saldo_matic):
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=matic-network&vs_currencies=eur')

    if response.status_code == 200:
        data = response.json()
        matic_price_in_eur = data['matic-network']['eur']
        saldo_eur = saldo_matic * matic_price_in_eur
        return saldo_eur
    else:
        print('Não foi possível obter a taxa de câmbio do MATIC para o Euro.')
        return None
