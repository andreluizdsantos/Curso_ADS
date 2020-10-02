# 28: Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
print('Vou pensar em um número entre 0 e 5, Tente adivinhar! \ncaso queira parar digite 9')
n = randint(0, 5)
while True:
    num = int(input('Digite um número: '))
    if n == num:
        print('Muito bem você acertou')
        n = randint(0, 5)
    elif num == 9:
        break
    else:
        print(f'Você errou, o número era: {n}, tente novamente')
        n = randint(0, 5)
"""
# 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
"""
v = float(input('Digite a velocidade do carro: '))
if v > 80:
    m = 7 * (v - 80)
    print(f'Você foi multado em R${m:.2f} por passar do limite de 80Km/h')
"""
# 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
num = int(input('Digite um número inteiro: '))
n = num % 2
if n == 0:
    print(f'O número {num} é Par!')
else:
    print(f'O número {num} é Ímpar!')
"""
# 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
# parta viagens mais longas.
"""
dist = int(input('Digite a distância da viagem em Km: '))
if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print(f'O valor da viagem será: R${preço}')
"""
# 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date
ano = int(input('Digite um ano para analisar se é Bissexto ou não: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano}, é Bissexto.')
else:
    print(f'O ano {ano}, não é Bissexto.')
"""
# 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor é: {maior}, e o menor é: {menor}')
"""
# 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    salario = salario * 1.1
    aumento = 10
else:
    salario = salario * 1.15
    aumento = 15
print(f'Você receberá um aumento de {aumento}% e seu salário será: R${salario:.2f}')
"""
# 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo
"""
ld1 = float(input('Digite o primeiro lado: '))
ld2 = float(input('Digite o segundo lado: '))
ld3 = float(input('Digite o terceiro lado: '))
if ld1 < ld2 + ld3 and ld2 < ld1 + ld3 and ld3 < ld1 + ld2:
    print('Sim pode formar um triângulo')
else:
    print('Não pode formar um triângulo')
"""
# Extra Cores - Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI
# para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m
# com todas as suas principais possibilidades.
print('\033[0;30;44m Estilo \033[m')
print('\033[1;30;44m Negrito \033[m')
print('\033[4;30;44m Sublinhado \033[m')
print('\033[7;30;44m Negativo \033[m')
print('\033[1;37;40m Fundo \033[m')
print('\033[1;30;41m Fundo \033[m')
print('\033[1;30;42m Fundo \033[m')
print('\033[1;30;43m Fundo \033[m')
print('\033[1;30;44m Fundo \033[m')
print('\033[1;30;45m Fundo \033[m')
print('\033[1;30;46m Fundo \033[m')
print('\033[1;30;47m Fundo \033[m')
print('\033[1;30;47m Texto \033[m')
print('\033[1;31;40m Texto \033[m')
print('\033[1;32;40m Texto \033[m')
print('\033[1;33;40m Texto \033[m')
print('\033[1;34;40m Texto \033[m')
print('\033[1;35;40m Texto \033[m')
print('\033[1;36;40m Texto \033[m')
print('\033[1;37;40m Texto \033[m')
