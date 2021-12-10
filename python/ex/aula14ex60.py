"""Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
 Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120"""
"""
from math import factorial
num = int(input("Digite um nomero para calcular seu fatorial: "))
print(f"O fatorial de {num} é {factorial(num)}")"""
"""
num = int(input("Digite um nomero para calcular seu fatorial: "))
fatorial = 1
print(f"Calculando {num}! = ", end='')
while num != 0:
    print(f"{num}", end='')
    print(" x " if num > 1 else " = ", end='')
    fatorial *= num
    num -= 1
print(f"{fatorial}")"""


def fatorial(x):
    f = 1
    while x != 0:
        print(f"{x}", end='')
        print(" x " if x > 1 else " = ", end='')
        f *= x
        x -= 1
    print(f"{f}")


num = int(input("Digite um nomero para calcular seu fatorial: "))
fatorial(num)
