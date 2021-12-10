"""Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    nas = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = ano - nas
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f"Pessoas maiores de idade: {maior}, e menores de idade: {menor}")
