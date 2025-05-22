#Faça um programa que leia um número qualquer e mostre o seu fatorial.
num = int(input("Digite um numero para saber seu fatorial: "))
cont = num
fat = 1
while cont > 1:
    fat*=cont
    cont-= 1
print(f"O fatorial do  {num} é {fat}")



