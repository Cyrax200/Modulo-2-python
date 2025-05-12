#A Confederação Nacional de Natação precisa de um programa que
#  leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
idade = 2025 - ano_nascimento

if   idade <= 9:
    print(f"Você tem {idade} anos, Categoria MIRIM")
elif idade <= 14:
    print(f"Você tem {idade} anos, Categoria INFANTIL")
elif idade <= 19:
    print(f"Você tem {idade} anos, Categoria JUNIOR")
elif idade <= 25:
    print(f"Você tem {idade} anos, Categoria SÊNIOR")
else:
    print(f"Você tem {idade} anos, Categoria MASTER")


