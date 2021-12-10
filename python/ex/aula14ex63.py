"""Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre
 na tela os N primeiros elementos de uma Sequência de Fibonacci.
  Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8"""

"""
n = int(input("Digite quantos elementos da sequência de Fibonacci que exibir: "))
cont = 3
t1 = 0
t2 = 1
print(f"{t1} {t2}", end=' ')
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, end=' ')
    cont += 1
"""

def fibonacci(x):
    if x == 0 or x == 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


n = int(input("Digite quantos elementos da sequência de Fibonacci que exibir: "))
cont = 0
while cont < n:
    print(fibonacci(cont), end=' ')
    cont += 1
