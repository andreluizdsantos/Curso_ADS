"""Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder, mostrando o total de
  vitórias consecutivas que ele conquistou no final do jogo."""
from random import randint
cont = tot = 0
print(10 *"=-=","\nVamos jogar par ou ímpar!")
while True:
    numj = int(input("Digite um valor: "))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input("Digite [P/I]: ")).strip().upper()[0]
    numc = randint(0, 10)
    tot = numj + numc
    print(f"O computador jogou: {numc} e o jogador jogou {numj}, total: {tot}", end= ' ')
    print("que é Par!" if tot % 2 == 0 else "que é Ímpar!")
    if escolha in 'P':
        if tot % 2 == 0:
            print("Jogador venceu!")
            cont += 1
        else:
            print("Computador venceu!")
            break
    elif escolha in 'I':
        if tot % 2 == 1:
            print("Jogador venceu!")
            cont += 1
        else:
            print("Computador venceu!")
            break
print(10 * "=-=")
print(f"Fim de jogo! O jogador venceu {cont} jogadas.")
