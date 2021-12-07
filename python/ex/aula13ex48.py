"""Exercício Python 48: Faça um programa que calcule a soma entre todos os números impares
 que são múltiplos de três e que se encontram no intervalo de 1 até 500."""
c = 0
s = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n
        c += 1
print(f"Total de númeoros impares multiplos de 3, no intervalo de 1 até 500: {c}. \nValor da soma dos números: {s}")
