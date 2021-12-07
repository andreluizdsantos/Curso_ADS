# 8 Escreva um programa que leia um valor em metros e exiba convertido em centímetros e em milimetros
m = float(input('Digite o valor em metros: '))
print('{}m corresponde a, {}cm e {}mm, e também a, {}dam, {}hm e {}Km'
      .format(m, (m * 100), (m * 1000), (m / 10), (m / 100), (m / 1000)))
