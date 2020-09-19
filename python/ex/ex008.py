# 16 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex.: Digite um número: 6.127 tem a parte Inteira: 6.
'''n = float(input('Digite um número Real qualquer: '))
print('A parte Inteira do número Real digitado é: {:.0f}'.format(n))'''

'''n = float(input('Digite um número Real qualquer: '))
print('A parte Inteira do número Real digitado é: {}'.format(int(n)))'''

'''from math import trunc
n = float(input('Digite um número Real qualquer: '))
print('A parte Inteira do número Real digitado é: {}'.format(trunc(n)))'''

# 17 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo,
# calcule e mostre o comprimento da hipotenusa.
'''ca = float(input('Comprimento Cateto adjacente: '))
co = float(input('Comprimento Cateto oposto: '))
print('O comprimento da Hipotenusa é: {}'.format(pow((ca**2+co**2), 1 / 2)))'''

'''from math import hypot
ca = float(input('Comprimento Cateto adjacente: '))
co = float(input('Comprimento Cateto oposto: '))
print('O comprimento da Hipotenusa é: {:.2f}'.format(hypot(ca, co)))'''

# 18 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, e cosseno e tangente, desse ângulo.
'''from math import radians, sin, cos, tan
a = float(input('Digite um ângulo qualquer: '))
print('Do ângulo {}°, o valor do seno é: {:.2f}, o valor do cosseno é: {:.2f}, e sua tangente {:.2f}'.format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))'''

# 19 Um professor que sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escreva o nome do escolhido.
'''from random import choice
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
alunos = [a1, a2, a3, a4]
print('O aluno sorteado é: {}'.format(choice(alunos)))'''

# 20 O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A ordem de alunos será: {}'.format(alunos))'''

# 21 Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
from pygame import mixer
mixer.init()
mixer.music.load('astronomia.mp3')
mixer.music.play()
input('Agora você escuta?')