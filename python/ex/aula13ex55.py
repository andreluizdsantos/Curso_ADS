"""Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos."""
pmaior = 0
pmenor = 0
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))
    if i == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        elif peso < pmenor:
            pmenor = peso
print(f"Maior peso: {pmaior}Kg\nMenor peso: {pmenor}Kg")
