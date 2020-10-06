# 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""valor = float(input('Digite o valor do emprestimo: '))
salario = float(input('Digite o valor do seu salario: '))
parc = int(input('Digite a quantidade de parcelas para pagar: '))
if valor / parc > (salario * 0.3):
    print('Emprestimo não pode ser autorizado!')
else:
    print(f'Emprestimo autorizado, valor da parcela será: R${valor / parc:.2f}')
"""
# 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""num = int(input('Digite um número inteiro: '))
while True:
    op = int(input('Escolha uma das bases para a conversão: \n[ 1 ] Base BINÁRIA:\n[ 2 ] Base OCTAL:\n[ 3 ] Base HEXADECIMAL:'))
    if op == 1:
        print(f'{num} convertido em BINÁRIO é: {bin(num)[2:]}')
    elif op == 2:
        print(f'{num} convertido em OCTAL é: {oct(num)[2:]}')
    elif op == 3:
        print(f'{num} convertido em HEXADECIMAL é: {hex(num)[2:]}')
    else:
        break
"""
# 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
"""n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'- O primeiro número é o maior!')
elif n2 > n1:
    print(f'- O segundo número é o maior!')
else:
    print('- Não exite valor maior, os dois são iguais!')
"""
# 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade == 18:
    print(f'Você tem {idade} anos e precisa fazer o alistamento Militar imediatamente!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento, que será em {nasc + 18}')
else:
    print(f'Seu alistamento já passou {idade - 18} anos e deveria ser feito em {nasc + 18}')
"""
# 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
"""n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'APROVADO! Sua média é {media:.1f}')
elif 7 > media >= 5: # elif media >= 5 and media <= 7:
    print(f'EM RECUPERAÇÂO! Sua média é {media:.1f}')
else:
    print(f'REPROVADO! Sua média é {media:.1f}')"""
# 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
"""from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
"""
# 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
# triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
"""ld1 = float(input('Digite o primeiro lado: '))
ld2 = float(input('Digite o segundo lado: '))
ld3 = float(input('Digite o terceiro lado: '))
if ld1 < ld2 + ld3 and ld2 < ld1 + ld3 and ld3 < ld1 + ld2:
    print('Sim pode formar um triângulo ', end='')
    if ld1 == ld2 == ld3:
        print('EQUILÁTERO!')
    elif ld1 == ld2 or ld1 == ld3 or ld2 == ld3:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Não pode formar um triângulo')
"""
# 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
"""peso = float(input('Digie seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.1f}', end='')
if imc < 18.5:
    print(' você está Abaixo do Peso')
elif 18.5 <= imc < 25:
    print(' você está no Peso Ideal')
elif 25 <= imc < 30:
    print(' você está com Sobrepeso')
elif 30 <= imc < 40:
    print(' você está com Obesidade')
else:
    print(' você está com Obesidade Mórbida')
"""
