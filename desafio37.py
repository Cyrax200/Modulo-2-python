#Escreva um programa em Python que leia um número inteiro qualquer e peça para o
#  usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input("Escreva um numero inteiro: "))
print("Escolha a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.")
base = int(input("escolha a base de conversão: "))

if base == 1:
    print(bin(num)[2:])
elif  base == 2:
    print(oct(num)[2:])
elif base == 3:
    print(hex(num)[2:])
else:
    print("Opção inválida")





