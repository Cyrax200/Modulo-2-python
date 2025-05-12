# Crie um programa que leia duas notas de um aluno e calcule sua média,
#  mostrando uma mensagem no final, de acordo com a média atingida:

notas = []
for i in range(2):
    nota  = float(input("Digite a nota do aluno: "))
    notas.append(nota)
media = (notas[0] + notas [1]) / 2

if media >= 7 and media <= 10:
    print(f"Você tirou {media}, Aluno aprovado")
elif media < 7 and media >= 5:
    print(f"você tirou {media}, esta de recuperação")
else:
    print(f" {media} REPROVADO")
