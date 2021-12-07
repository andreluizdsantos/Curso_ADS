# 10 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ 1,00 = R$ 3,27 ;( *2017 , R$ 5,36 em 2020.
r = float(input('Digite um valor em Reais: '))
d = float(input('Digite o valor do Dólar na cotação atual: '))
e = float(input('Digite o valor do Euro na cotação atual: '))
print('Valor de R${:.2f} é equivalente a US${:.2F} e a €{:.2f}'.format(r, r / d, r / e))
