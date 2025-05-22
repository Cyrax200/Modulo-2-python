#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão "))

contador = 0

while contador < 10:
        print(termo, end=" → ")
        termo+=razao
        contador+=1
print('FIM')
    

