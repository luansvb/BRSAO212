#1 - Crie um programa que lê um arquivo CSV com a biblioteca pandas,
#calcule e exiba a média e o desvio padrão da coluna tempo_execucao,
#caso o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro.

import pandas as pd

arquivo = input("Digite o nome do arquivo CSV: ")

try:
    df = pd.read_csv(arquivo)

    media = df["tempo_execucao"].mean()
    desvio = df["tempo_execucao"].std()

    print("Média:", round(media, 2))
    print("Desvio padrão:", round(desvio, 2))

except:
    print("Erro ao ler o arquivo.")