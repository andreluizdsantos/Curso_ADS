"""Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número
 que o usuário escolher, só que agora utilizando um laço for."""
n1 = int(input('Digite um número inteiro qualquer: '))
print(f' A tabuada de {n1} é:\n', '=' * 16)
for n in range(1, 11):
    print(f' |{n1:>3} x{n:>3} ={n * n1:>3} |')
print('', '=' * 16)
