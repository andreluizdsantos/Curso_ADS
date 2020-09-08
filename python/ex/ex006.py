# Desafio 04 Guanabara
num = 'Não!'
alpha = 'Não!'
alnum = 'Não!'
space = 'Não!'
a = input('Digite algo: ')
print('O tipo primitido deste valor é', type(a))
if (a.isnumeric() == True):
    num = 'Sim!'
print('É numérico? {}'.format(num))
if (a.isalpha() == True):
    alpha = 'Sim!'
print('É alfabético? {}'.format(alpha))
if (a.isalnum() == True):
    alnum = 'Sim!'
print('É alfanumérico? {}'.format(alnum))
if (a.isspace() == True):
    space = 'Sim!'
print('Só tem espaço? {}'.format(space))
print('Está em maiúsculas? {}'.format(a.isupper()))
print('Está em minúsculas? {}'.format(a.islower()))
print('Está capitalizada? {}'.format(a.istitle()))