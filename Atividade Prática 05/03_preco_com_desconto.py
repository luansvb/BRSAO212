#3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
#a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
#b - Preço final: Determina o novo preço após o desconto.
#c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
#d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

preco_original = float(input("Digite o preço do produto: "))
porcentagem = float(input("Digite a porcentagem de desconto: "))

valor_desconto = preco_original * (porcentagem / 100)
preco_final = preco_original - valor_desconto

print("Preço original: R$", round(preco_original, 2))
print("Desconto aplicado: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))