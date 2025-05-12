#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
nome = str(input("Digite seu nome: "))
ano_nascimento = int(input("Digite o ano em que você nasceu: "))
ano_atual = 2025
idade = ano_atual - ano_nascimento

if idade == 18:
    print(f"{nome} sua idade é {idade} anos, Você deve se alistar")
elif idade < 18:
    print(f"{nome} sua idade é {idade} anos, você ainda vai se alistar")
    print(f" Faltam {18 - idade} anos para você se alistar")
    print(f"seu alistamento será em {(18 -idade)+ 2017}")
elif idade >= 45:
    print(f"{nome} sua idade é {idade} anos, você já passou do tempo de se alistar")
    print(f"você passou {idade - 18} anos, do alistamento correto")
elif idade > 18:
    print(f"{nome} sua idade é {idade} anos,  Você já devia ter se alistado a {idade - 18} ano atrás:")