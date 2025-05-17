#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesos = []
cont = 0 
for pessoas in range(1,6):
    p = int(input("Qual seu peso? "))
    pesos.append(p)
    cont +=1
    print(f"Peso da {cont}° pessoa: {p}")
print(f"O maior peso {max(pesos)} e o menor peso {min(pesos)}")

    

