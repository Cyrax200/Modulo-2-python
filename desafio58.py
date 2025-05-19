#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
num = 0
jogador = 0
cont = 0

num = randint(0,10)
print("Advinhe um número entre 0 a 10!")
while jogador != num:
 cont+= 1
 jogador =  int(input("Numero incorreto , digite novamente "))
print(f"Você acertou o computador digitou {num}, você teve {cont} tentativas para acertar")






