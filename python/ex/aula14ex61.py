"""Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while."""
print("Gerador de PA")
p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
t = 1
while t <= 10:
    print(p, end=' ')
    p += r
    t += 1
