#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
p =  int(input("Primeiro termo: "))
r = int(input("Razão: "))
d = p + (10 -1) * r
for n in range(p,d + r,r):
    print(n,end= " -> ")
print("FIM")