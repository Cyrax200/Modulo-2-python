#Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
for i in range(7):
    nasc = int(input('Em que ano você nasceu? '))
    idade = ano_atual - nasc
    if idade >= 21:
        print('Você é de maior')
    else:
        print("Você é de menor")