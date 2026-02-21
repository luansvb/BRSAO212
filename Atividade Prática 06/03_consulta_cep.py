#3 - Crie um programa que consulte informações de um CEP na API,
#retorne logradouro, bairro, cidade e estado do CEP digitado,
#caso o CEP não existir ou houver erro na requisição,
#mostre uma mensagem de falha.

import requests

cep = input("Digite o CEP: ")

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("Logradouro:", dados["logradouro"])
        print("Bairro:", dados["bairro"])
        print("Cidade:", dados["localidade"])
        print("Estado:", dados["uf"])

except:
    print("Erro na requisição.")