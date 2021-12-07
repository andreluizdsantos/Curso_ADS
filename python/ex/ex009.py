# 9 Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
n1 = int(input('Digite um número inteiro qualquer: '))
n = 1
print('  A tabuada de {} é:\n'.format(n1), '=' * 18)
while n <= 10:
    print(' |{:>3} x {:>3} = {:>3} |'.format(n1, n, n * n1))
    n = n + 1
print('','=' * 18)
