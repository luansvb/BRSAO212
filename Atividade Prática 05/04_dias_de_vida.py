#4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
data_atual = datetime.today()

diferenca = data_atual - data_nascimento

print("Você está vivo há", diferenca.days, "dias.")