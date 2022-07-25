"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
 e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""
notas = [50, 20, 10, 1]
def linha():
    print(40 * '=')
while True:
    saque = [0, 0, 0, 0]
    op = ' '
    linha()
    print("{: ^40}".format("Banco ALS"))
    linha()
    valor = int(input("Que valor quer sacar: R$"))
    for i in range(4):
        saque[i] = int(valor / notas[i])
        valor = valor % notas[i]
        if (saque[i] != 0):
            if (saque[i] > 1):
                print(f"Total de {saque[i]} cédulas de R${notas[i]},00")
            else:
                print(f"Total de {saque[i]} cédula de R${notas[i]},00")
    linha()
    while op not in 'NS':
        op = str(input("Novo saque? [S/N] ")).strip().upper()[0]
    if (op in 'N'):
        break
