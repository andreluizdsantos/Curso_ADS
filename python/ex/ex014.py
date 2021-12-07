# 14 Faça um programa que calcule a temperatura em °F a partir de °C
c = float(input('Digite a temperatura em °C: '))
print('A temperatura de {}°C graus Celsius corresponde a {}'
      '°F graus Fahrenheit e {}K em Escala Kelvin.'.format(c, ((c * 9) / 5) + 32, c + 273,15))
