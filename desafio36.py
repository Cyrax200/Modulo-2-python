#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
# o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa que você deseja comprar: "))
salario_comprador = float(input("Digite o valor do seu salário: "))
parcelas_anos = float(input("Em quantos anos você deseja pagar: "))

prestacao = valor_casa / (parcelas_anos * 12)
porcentagem = salario_comprador * 30 / 100

print(f"para pegar uma casa no valor de  R${valor_casa:.2f} em {parcelas_anos} anos, a prestação será no valor de R$:{prestacao:.2f}")

if prestacao <= porcentagem:
     print("Emprestimo autorizado")
else:
     print("Emprestimo  negado!")



