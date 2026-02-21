#2 - Criar um código que registre as notas de alunos e calcular a média da turma.

quantidade = int(input("Digite a quantidade de alunos: "))

soma = 0

for i in range(quantidade):
    nota = float(input("Digite a nota do aluno: "))
    soma += nota

media = soma / quantidade

print("Média da turma:", round(media, 2))