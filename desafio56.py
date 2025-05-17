#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a menor  idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
total_pessoas = []
total_idades = []
menor_idade = 0
maior_idade = 0
homem_mais_velho = {'nome': '', 'idade':0}
mulheres_menores_20 = 0
cont = 0

for p in range(1,5):
    cont+= p
    print(f"---{p}° PESSOA---")
    nome = str(input("Nome: ")).upper().strip()
    idade = int(input("Idade: "))
    sexo = str(input("[F] para Feminino e [M] para Masculino: ")).upper()
   

    pessoas = {
        'nome': nome,
        'idade':idade,
        'sexo':sexo
    }

    total_pessoas.append(pessoas)
    total_idades.append(idade)
    maior_idade = max(total_idades)
    menor_idade = min(total_idades)
    

    if sexo == 'F' and idade < 20:
        mulheres_menores_20+= 1

    if sexo == 'M' and idade > homem_mais_velho['idade']:
        homem_mais_velho['nome'] = nome
        homem_mais_velho['idade'] = idade
        
print(f"A menor idade do grupo é {menor_idade}")

if homem_mais_velho['nome']:
    print(f"O homem mais velho é {homem_mais_velho['nome']} com {homem_mais_velho['idade']} anos.")
else:
    print("não há homens no grupo.")

print(f"{mulheres_menores_20} mulher(es) têm menos de 20 anos.")
    
        



    

       
    









    



 





 
    

