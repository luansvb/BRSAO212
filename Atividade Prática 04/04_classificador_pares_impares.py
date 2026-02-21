#4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares
#e contabilizando quantos de cada tipo foram inseridos.

quantidade = int(input("Quantos números você deseja inserir? "))

pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        print("Número par")
        pares += 1
    else:
        print("Número ímpar")
        impares += 1

print("Total de números pares:", pares)
print("Total de números ímpares:", impares)