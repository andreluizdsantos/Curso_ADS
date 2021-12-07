# 18 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, e cosseno e tangente, desse ângulo.
from math import radians, sin, cos, tan
a = float(input('Digite um ângulo qualquer: '))
print('Do ângulo {}°, o valor do seno é: {:.2f},'
      ' o valor do cosseno é: {:.2f}, e sua tangente {:.2f}'
      .format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))
