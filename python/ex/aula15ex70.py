"""Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""
produto = maisbarato = ""
total = menorvalor = cont = 0
print("",40 * "-","\n","{: ^40}".format("LOJA SUPER BARATÃO"),"\n",40 * "-")
while True:
    produto = str(input("Nome do Produto: "))
    valor = float(input("Preço: R$"))
    total += valor
    opcao = ' '
    if (valor >= 1000):
        cont += 1
    if (valor < menorvalor or menorvalor == 0):
        menorvalor = valor
        maisbarato = produto
    while opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao in 'N':
        break
print("{:-^40}".format("FIM DO PROGRAMA"))
print(f"O total  da compra foi R${total:.2f}")
print(f"Temos {cont} produtos custanto mais de R$1000.00")
print(f"O produto mais barato foi {maisbarato} que custa R${menorvalor:.2f}")
