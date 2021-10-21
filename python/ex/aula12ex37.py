# 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
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
