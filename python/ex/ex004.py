print(30*'=', '\n ========= DESAFIO 03 =========\n', 31*'=') # \n para pular linha
n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2), end=' ') # end=' ' para não pular linha e dar um espaço
print('e a subtração de {} por {} é igual a {}'.format(n1, n2, n1 - n2))
print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
print('A divisão de {} por {} é igual a {}'.format(n1, n2, n1 / n2))
print('A divisão inteira de {} por {} é igual a {}'.format(n1, n2, n1 // n2))
print('O produto da divisão entre {} por {} é {}'.format(n1, n2, n1 % n2))
print('O número {} elevado a {} é igual a {}'.format(n1, n2, n1 ** n2))
print('A raiz quadrada de {} é {} e a de {} é {}'.format(n1, n1 ** (1/2), n2, n2 ** (1/2)))
print('\nE a tabuada de {} é:'.format(n1))
n = 1
while n <= 10:
    print('{} X {} = {}'.format(n, n1, n1 * n))
    n = n + 1
print('\nE a tabuada de {} é:'.format(n2))
n = 1
while n <= 10:
    print('{} X {} = {}'.format(n, n2, n2 * n))
    n = n + 1
