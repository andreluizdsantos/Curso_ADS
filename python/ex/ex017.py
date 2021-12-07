# 17 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo,
# calcule e mostre o comprimento da hipotenusa.
"""ca = float(input('Comprimento Cateto adjacente: '))
co = float(input('Comprimento Cateto oposto: '))
print('O comprimento da Hipotenusa é: {}'.format(pow((ca**2+co**2), 1 / 2)))"""

from math import hypot
ca = float(input('Comprimento Cateto adjacente: '))
co = float(input('Comprimento Cateto oposto: '))
print('O comprimento da Hipotenusa é: {:.2f}'.format(hypot(ca, co)))
