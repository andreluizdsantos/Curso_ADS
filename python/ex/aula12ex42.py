# 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
# triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
ld1 = float(input('Digite o primeiro lado: '))
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
