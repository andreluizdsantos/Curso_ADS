#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
escolha = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
jogador = int(input("""Jogue:
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura
""")) - 1
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
if computador == 0:
    if jogador == 0:
        print(f"Empate! {escolha[computador]} x {escolha[jogador]}")
    elif jogador == 1:
        print(f"Jogador ganhou! {escolha[computador]} é coberta pelo {escolha[jogador]}")
    elif jogador == 2:
        print(f"Computador ganhou! {escolha[computador]} quebra {escolha[jogador]}")
elif computador == 1:
    if jogador == 0:
        print(f"Computador ganhou! {escolha[computador]} cobre {escolha[jogador]}")
    elif jogador == 1:
        print(f"Empate! {escolha[computador]} x {escolha[jogador]}")
    elif jogador == 2:
        print(f"Jogador ganhou! {escolha[computador]} é cortado pela {escolha[jogador]}")
elif computador == 2:
        if jogador == 0:
            print(f"Jogador ganhou! {escolha[computador]} é quebrada pela {escolha[jogador]}")
        elif jogador == 1:
            print(f"Computador ganhou! {escolha[computador]} corta {escolha[jogador]}")
        elif jogador == 2:
            print(f"Empate! {escolha[computador]} x {escolha[jogador]}")
else:
    print("Opção inválida:")
