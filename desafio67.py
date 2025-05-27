#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#  O programa será interrompido quando o número solicitado for negativo. 
while True:
    
    tab = int(input('Digit eum numero para saber a tabuada: '))
    print('digite um numero negativo para encerrar o programa')
    if tab < 0:
        break
    for n in range(1,11):
        print(f'{tab} x {n} = {tab * n}')
print('FIM')
        
    

    