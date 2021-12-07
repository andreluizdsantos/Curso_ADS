# 15 Exercício Python 15: Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
qdias = int(input('Digite a quantidade de dias o carro foi alugado: '))
km = float(input('Digite a quilometragem rodada com o veículo: '))
print('O valor total a pagar por {}'
      ' dias de aluguel e {}km rodados, é R${:.2f}'.format(qdias, km, ((qdias * 60) + (km * 0.15))))
