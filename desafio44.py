"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros"""


valor_produto = float(input("Digite o valor do produto: "))
opcao = int(input(" [1] á vista dinheiro/ cheque \n [2] á vista cartão \n [3] 3x ou mais no cartão \n [4] 2x no cartão \n qual opção deseja? "))


if opcao == 1:
    print(f"{ valor_produto - (valor_produto * .10) }")
elif opcao == 2:
    print(f"{valor_produto - (valor_produto * .05)}")
elif opcao == 3:
    print(f"{valor_produto * .20 + valor_produto}")
elif opcao == 4:
    print(f"{valor_produto}")