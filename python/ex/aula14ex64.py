"""Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
  No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""
"""
num = int(input("Digite um número [999 para parar]: "))
soma = cont = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: "))
print(f"Foram digitados {cont} números, que a soma é: {soma}")
"""

num = soma = cont = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"Foram digitados {cont} números, que a soma é: {soma}")