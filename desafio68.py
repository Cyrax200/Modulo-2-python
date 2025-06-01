#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, 
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

import random

play = 1
computador  = 1
while  True:
    cond = str(input("Escolha Impar ou Par: ")).upper().rstrip()
    play = int(input("Digite um numero: "))
    computador = random.randint(0,10)
    print(computador)
    total = play + computador
    if cond == 'PAR':
        if total %  2 == 0:
            print("Você ganhou")
        else:
            print("Você perdeu")
            break
    elif cond == 'IMPAR':
        if total % 2 != 0:
            print("Você ganhou")
        else:
            print('Você perdeu')
            break
    
        
        




