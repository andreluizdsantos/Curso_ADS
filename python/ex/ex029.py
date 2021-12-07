# 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Digite a velocidade do carro: '))
if v > 80:
    m = 7 * (v - 80)
    print(f'Você foi multado em R${m:.2f} por passar do limite de 80Km/h')
