# 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

"""nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome com letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome é: {}'.format(nome[:nome.find(' ')]))
separa = nome.split()
print('Seu primeiro nome é: {}, e tem {} letras.'.format(separa[0], len(separa[0])))"""

# 23 - Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

"""num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Milhar: {}, centena: {}, dezena: {}, unidade: {}'.format(m, c, d, u))"""

# 24 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""cid = str(input('Digite o nome da cidade que você nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')"""

# 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))"""

#26 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra
# “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""frase = str(input('Digite uma frase: ')).strip().upper()
print('A frase tem {} letras "A".'.format(frase.count('A')))
print('A primeira letra "A" aparece na posição: {}.'.format(frase.find('A') + 1))
print('A ultima letra "A" aparece na posição: {}.'.format(frase.rfind('A') + 1))"""

# 27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer {}!'.format(n))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome) - 1]))
