#Crie um programa que leia dois valores e mostre um menu na tela:
"""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outor numero: "))


while True:
    opcao = int(input(" Escolha\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n"))
    if opcao == 2:
        print(f'você escolheu multiplicar, resultado: {num1*num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f"o numero maior é {num1}")
        else:
            print(f"O numero maior é {num2}")
    elif opcao == 4:
        print('Digite os numeros novamente')
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outor numero: "))
    else:
        print("Sair do programa")
        break
    
