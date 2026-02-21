#4 - Crie um programa que realize consultas em relação ao Real (BRL) usando a API
#mostre valor atual, máxima, mínima e data/hora da última atualização,
#caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

import requests

moeda = input("Digite a moeda desejada (ex: USD, EUR): ")

try:
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    dados = resposta.json()

    chave = moeda + "BRL"

    if chave in dados:
        info = dados[chave]

        print("Valor atual:", info["bid"])
        print("Máxima:", info["high"])
        print("Mínima:", info["low"])
        print("Última atualização:", info["create_date"])
    else:
        print("Moeda não encontrada.")

except:
    print("Erro na requisição.")