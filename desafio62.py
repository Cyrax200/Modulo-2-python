#perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão "))
contador = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador != total:
            print(termo, end=" → ")
            termo+=razao
            contador+=1 
    print("Pausa")
    mais = int(input("quantos termos você quer mostrar a mais? "))
print("FIM")