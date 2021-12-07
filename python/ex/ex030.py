# 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número inteiro: '))
n = num % 2
if n == 0:
    print(f'O número {num} é Par!')
else:
    print(f'O número {num} é Ímpar!')
