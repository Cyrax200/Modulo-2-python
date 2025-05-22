#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'.upper().strip()
contador = 0
n = 0
soma = 0
while continuar == 'S':
    n = int(input('Digite um numero: '))
    soma+=n
    contador += 1
    media = soma / contador
    continuar = str(input('Deseja continuar ? [S] para sim e [N] para não: ')).upper().strip()
    if continuar  == 'N':
        print(f"a quantidade de numeros digitados {contador} numeros , a media dos numeros: {media} ")


