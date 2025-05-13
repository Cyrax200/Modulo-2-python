"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes"""

r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo!")
    
    if r1 == r2 == r3:
        print("EQUILÁTERO: todos os lados são iguais")
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print("ESCALENO: todos os lados são diferentes")
    else:
        print("ISÓSCELES: dois lados iguais")
else:
    print("Os segmentos acima não podem formar um triângulo")
