#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

if num1 > num2:
    print(f"O numero {num1} é maior que o numero {num2}")
elif num2 > num1:
    print(f"O numero {num2} é maior que o numero {num1}")
else:
    print("Os dois numeros são iguais")
