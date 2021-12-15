"""Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder, mostrando o total de
  vitórias consecutivas que ele conquistou no final do jogo."""
from random import randint
numc = randint(0,10)
cont = result = 0
print(10 *"=-=","\nVamos jogar par ou ímpar!")
while True:
    numj = int(input("Digite um valor: "))
    escolha = str(input("Digite [P/I]: ")).strip().lower()[0]
    if escolha in 'p':
        jog = 0
        comp = 'ímpar'
    else:
        jog = 1
        comp = 'par'
    if (numj + numc) % 2 == 0:
        result = 0
    else:
        result = 1
    if result == jog:
        print("Jogador venceu!")
        print(f"O computador escolheu {comp} e jogou: {numc}")
        cont += 1
    else:
        print("Computador venceu!")
        break
    print(10 * "=-=")
print(f"Jogador venceu {cont} jogadas.")
print(f"O computador escolheu {comp} e jogou: {numc}")