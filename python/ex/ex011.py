""" 11 Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua àrea e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, cobre uma àrea de 2m²"""

l = float(input('Digite o valor da largura da parede em metro(s): '))
a = float(input('Digite o valor da altura da parede em metro(s): '))
print('A área da parede é de {}m².'.format(l * a))
print('Será necessário {}litro(s) de tinta'.format((l * a) / 2))