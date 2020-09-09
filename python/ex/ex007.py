# ========== Desafio 5 ==========
# 5 Faça um programa que leia um numero inteiro e mostre seu sucessor e seu antecessor
n = int(input('Digite um número: '))
print('O número digitado é {}, seu antecessor é {}, e seu sucessor é {}.'.format(n , n - 1, n + 1))

# 6 Criar um programa que leia um numero e mostre o seu dobro, seu triplo e a raiz quadrada
print('O dobro de {} é {}, seu triplo é {}, e sua raiz quandrada é {}'.format(n, 2 * n, 3 * n, n ** (1/2)))

# 7 Desenvolva um programa que leia as duas notas de um aluno e mostre a sua média
nt1 = float(input('Digite sua primeira nota: '))
nt2 = float(input('Digite sua segunda nota: '))
print('Sua média é {:.2f}.'.format((nt1 + nt2) / 2))

# 8 Escreva um programa que leia um valor em metros e exiba convertido em centímetros e em milimetros
m = float(input('Digite o valor em metros: '))
print('{}m corresponde a, {}cm e {}mm, e também a, {}dam, {}hm e {}Km'.format(m, (m * 100), (m * 1000), (m / 10), (m / 100), (m / 1000)))

# 9 Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
n1 = int(input('Digite um número inteiro qualquer: '))
n = 1
print('A tabuada de {} é:\n'.format(n1), '=' * 18)
while n <= 10:
    print('|{:>3} x {:>3} = {:>3} |'.format(n1, n, n * n1))
    n = n + 1
print('=' * 18)

# 10 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27 ;( *2017 , R$ 5,36 em 2020.
r = float(input('Digite um valor em Reais: '))
d = float(input('Digite o valor do Dólar na cotação atual: '))
e = float(input('Digite o valor do Euro na cotação atual: '))
print('Valor de R${} é equivalente a US${} e a €{}'.format(r, r / d, r / e))

# 11 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua àrea e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, cobre uma àrea de 2m²
l = float(input('Digite o valor da largura da parede em metro(s): '))
a = float(input('Digite o valor da altura da parede em metro(s): '))
print('A área da parede é de {}m².'.format(l * a))
print('Será necessário {}litro(s) de tinta'.format((l * a) / 2))

# 12 Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p = float(input('Digite o preço do produto: '))
print('O valor com 5% de desconto é R${:.2f} reais'.format(p - (p * 0.05)))
""" {:.2f} recebeu a formatação para exibir o valor com duas casas decimais após a virgula e que terá como saída um valor float """

# 13 Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite o valor do salário: R$ '))
print('Valor com reajuste de 15%, R$ {:.2f}'.format(s * 1.15))

# 14 Faça um programa que calcule a temperatura em °F a partir de °C
c = float(input('Digite a temperatura em °C: '))
print('A temperatura de {}°C graus Celsius corresponde a {}°F graus Fahrenheit e {}K em Escala Kelvin.'.format(c, ((c * 9) / 5) + 32, c + 273,15))