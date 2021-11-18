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
        print("Empate! {} x {}".format(escolha[computador], escolha[jogador]))
    elif jogador == 1:
        print("Jogador ganhou! {} cobre {}".format(escolha[computador], escolha[jogador]))
    elif jogador == 2:
        print("Computador ganhou! {} quebra {}".format(escolha[computador], escolha[jogador]))
elif computador == 1:
    if jogador == 0:
        print("Computador ganhou! {} cobre {}".format(escolha[computador], escolha[jogador]))
    elif jogador == 1:
        print("Empate! {} x {}".format(escolha[computador], escolha[jogador]))
    elif jogador == 2:
        print("Jogador ganhou! {} é cortado pela {}".format(escolha[computador], escolha[jogador]))
elif computador == 2:
        if jogador == 0:
            print("Jogador ganhou! {} é quebrada pela {}".format(escolha[computador], escolha[jogador]))
        elif jogador == 1:
            print("Computador ganhou! {} corta {}".format(escolha[computador], escolha[jogador]))
        elif jogador == 2:
            print("Empate! {} x {}".format(escolha[computador], escolha[jogador]))
else:
    print("Opção inválida:")
