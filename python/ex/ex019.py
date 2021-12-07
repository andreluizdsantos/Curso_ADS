# 19 Um professor que sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escreva o nome do escolhido.
from random import choice
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
alunos = [a1, a2, a3, a4]
print('O aluno sorteado é: {}'.format(choice(alunos)))