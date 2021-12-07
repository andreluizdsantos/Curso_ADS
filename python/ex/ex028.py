# 28: Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
print('Vou pensar em um número entre 0 e 5, Tente adivinhar! \ncaso queira parar digite 9')
n = randint(0, 5)
while True:
    num = int(input('Digite um número: '))
    if n == num:
        print('Muito bem você acertou')
        n = randint(0, 5)
    elif num == 9:
        break
    else:
        print(f'Você errou, o número era: {n}, tente novamente')
        n = randint(0, 5)
