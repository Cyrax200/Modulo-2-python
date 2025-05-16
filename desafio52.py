#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input("Digite um numero: "))
total = 0
for i in range(1,n+1):
    if n % i == 0:
        print(i)
        total += 1
if total == 2:
    print(f"O numero foi dividido {total}, ele é primo")
else:
    print(f"O numero foi dividido {total}, ele não é primo")

    