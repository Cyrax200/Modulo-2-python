#Crie um programa que faça o computador jogar Jokenpô com você.
import random
jogador = int(input("Escolha \n[0] para PEDRA\n[1] para PAPEL\n[2] para TESOURA. \n\n"))
computador = random.randint(0,2)


if jogador == 0 and computador == 1:
    print("Jogador jogou PEDRA\nComputador jogou PAPEL\n")
    print("jogador perdeu")
elif jogador == 0 and computador == 2:
    print("Jogador jogou PEDRA\nComputador jogou TESOURA\n")
    print("Jogador ganhou")
elif jogador == 2 and computador == 1:
    print("Jogador jogou TESOURA\nComputador jogou PAPEL\n")
    print("jogador ganhou")
elif jogador  == 2 and computador == 0:
    print("jogador perdeu")
else:
    print("jogue novamente")