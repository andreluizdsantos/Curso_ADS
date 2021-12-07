# 16 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex.: Digite um número: 6.127 tem a parte Inteira: 6.
"""n = float(input('Digite um número Real qualquer: '))
print('A parte Inteira do número Real digitado é: {:.0f}'.format(n))

n = float(input('Digite um número Real qualquer: '))
print('A parte Inteira do número Real digitado é: {}'.format(int(n)))"""

from math import trunc
n = float(input('Digite um número Real qualquer: '))
print('A parte Inteira do número Real digitado é: {}'.format(trunc(n)))
