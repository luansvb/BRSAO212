#2 - Crie um programa que acesse a API para buscar um usuário fictício aleatório.
#exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão,
#mostre uma mensagem de falha.

import requests

try:
    resposta = requests.get("https://randomuser.me/api/")
    dados = resposta.json()

    usuario = dados["results"][0]

    nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)

except:
    print("Falha ao conectar à API.")