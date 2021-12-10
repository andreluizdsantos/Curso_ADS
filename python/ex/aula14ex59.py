"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep

op = 0


def soma(x, y):
    return x + y


def multiplicacao(x, y):
    return x * y


def maior(x, y):
    if x > y:
        return f" Entre {x} e {y}, {x} é o maior!"
    elif x < y:
        return f" Entre {x} e {y}, {y} é o maior!"
    else:
        return f" Entre {x} e {y}, eles são iguais"


n1 = int(input(" Digite o primeiro número: "))
n2 = int(input(" Digite o segundo número: "))

while op != 5:
    op = int(input(""" [ 1 ] Somar
 [ 2 ] Multiplicar
 [ 3 ] Maior
 [ 4 ] Novos números
 [ 5 ] Sair do programa
 Digite uma opção: """))
    if op == 1:
        print(f" A soma de {n1} e {n2} é: {soma(n1, n2)}")
    elif op == 2:
        print(f" A multiplicação de {n1} por {n2} é: {multiplicacao(n1, n2)}")
    elif op == 3:
        print(maior(n1, n2))
    elif op == 4:
        n1 = int(input(" Digite o primeiro número: "))
        n2 = int(input(" Digite o segundo número: "))
    else:
        print("Opção inválida!")
    print(10 * "=-=")
    sleep(2)
print("Fim do Programa!")
