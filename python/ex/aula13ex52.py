"""Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""
n = int(input("Digite um número: "))
c = 0
for i in range(1, n +1):
    if n % i == 0:
        c += 1
        print(f'\033[1;31;40m {i} \033[m', end="")
    else:
        print(f'\033[1;33;40m {i} \033[m', end="")
if c == 2:
    print(f"\nÉ um número primo, foi divisível {c} vezes")
else:
    print(f"\nNão é um número primo, foi divisível {c} vezes")
