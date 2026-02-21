#2 - Crie um programa que cria um arquivo TXT com nome, idade e cidade de algumas pessoas,
#que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário,
#caso ocorra um erro ao salvar, mostre uma mensagem de falha.

nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.txt): ")

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", "25", "São Paulo"],
    ["Carlos", "30", "Rio de Janeiro"],
    ["Mariana", "22", "Curitiba"]
]

try:
    with open(nome_arquivo, "w") as arquivo:
        for linha in dados:
            arquivo.write("\t".join(linha) + "\n")

    print("Arquivo salvo com sucesso.")

except:
    print("Erro ao salvar o arquivo.")