# 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo

ld1 = float(input('Digite o primeiro lado: '))
ld2 = float(input('Digite o segundo lado: '))
ld3 = float(input('Digite o terceiro lado: '))
if ld1 < ld2 + ld3 and ld2 < ld1 + ld3 and ld3 < ld1 + ld2:
    print('Sim pode formar um triângulo')
else:
    print('Não pode formar um triângulo')
