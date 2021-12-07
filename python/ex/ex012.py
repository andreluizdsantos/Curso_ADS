# 12 Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p = float(input('Digite o preço do produto: '))
print('O valor com 5% de desconto é R${:.2f} reais'.format(p - (p * 0.05)))
""" {:.2f} recebeu a formatação para exibir o valor com duas casas
 decimais após a virgula e que terá como saída um valor float """
