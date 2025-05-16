#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input("Digite uma frase para saber se ela é palindromo: ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
if inverso == junto:
        print(f'{frase} == {inverso} palindromo')
else:
        print(f'{frase} == {inverso} não é um palindromo')

