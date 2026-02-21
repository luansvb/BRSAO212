#4 - Crie um programa que leia e escreva arquivos no formato JSON,
#que salve em um dicionário com nome, idade e cidade em um arquivo JSON
#e depois leia o mesmo arquivo exibindo os dados,
#caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.

import json

dados = {
    "nome": "João",
    "idade": 28,
    "cidade": "Belo Horizonte"
}

nome_arquivo = "dados.json"

try:
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo)

    with open(nome_arquivo, "r") as arquivo:
        dados_lidos = json.load(arquivo)

    print("Dados lidos do arquivo:")
    print("Nome:", dados_lidos["nome"])
    print("Idade:", dados_lidos["idade"])
    print("Cidade:", dados_lidos["cidade"])

except:
    print("Erro ao salvar ou ler o arquivo.")