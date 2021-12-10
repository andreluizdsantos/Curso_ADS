"""Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
 em um número entre 0 e 10.  Só que agora o jogador vai tentar adivinhar até acertar,
  mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
print("Vou pensar em um número entre 0 e 10, tente adivinhar!")
num = randint(0, 10)
# print(num)
palpite = int(input("Digite um número: "))
cont = 1
while palpite != num:
    if palpite < num:
        print("Mais... ", end='')
    else:
        print("Menos... ", end='')
    palpite = int(input("Outro número: "))
    cont += 1
print(f"Acertou! O número é {num}.\nNúmero de tentativas: {cont}")
