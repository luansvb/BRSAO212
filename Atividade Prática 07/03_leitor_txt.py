#3 - Crie um programa que leia um arquivo TXT informado pelo usuário,
#percorrendo cada linha do arquivo e a exibe na tela,
#caso o arquivo não seja encontrado, mostre uma mensagem de erro.

nome_arquivo = input("Digite o nome do arquivo para ler: ")

try:
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())

except:
    print("Arquivo não encontrado.")
    