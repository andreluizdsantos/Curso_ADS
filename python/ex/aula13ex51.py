"""Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a
 razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""
prm = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão da PA: "))
n = raz * 10
for i in range(prm, n, raz):
    print(i, end=" ")
