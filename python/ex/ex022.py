# 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome com letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome é: {}'.format(nome[:nome.find(' ')]))
separa = nome.split()
print('Seu primeiro nome é: {}, e tem {} letras.'.format(separa[0], len(separa[0])))
