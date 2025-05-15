# mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input("Digite um numero para saber a tabuada: "))
for n in range(0,11):
    tabuada = n * numero
    print(f"{numero} x {n} = {tabuada} ")