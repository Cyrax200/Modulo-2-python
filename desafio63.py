#Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
n = int(input("quantos termos? "))
cont = 1
t1,t2 = 0,1


while cont <= n:
    print(t1,end= " -> ")
    t1,t2 = t2,t1 +t2
    cont+=1