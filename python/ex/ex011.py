def ope(x, y):
    ad = x + y
    su = x - y
    mu = x * y
    di = x / y
    return ad, su, mu, di

print('Inicio do programa')
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
s = ope(a, b)
print(f'Soma: {s[0]}, Subritração: {s[1]}, Multiplicação: {s[2]}, Divisão: {s[3]}')

lista = ['Lista', 'é mutável' , 'pode receber novos valores', 'e é sequencial inicia em 0 e vai a n - 1']
lista1 = [] # pode ser criada sem valor
lista2 = list(2*x for x in range(10)) # pode ser criada usando list() comprehension, com for in, Sua sintaxe básica é:
# [item for item in lista]
print(lista, lista1, lista2)
tupla = ('Tuplas', 'Imutável ', 'Não permite insersão ', 'mas pode ser acessado pela posição ', 'na sequência')
print(tupla)
set = {'Set', 'permite adicionar', 'valores usando a função add() ', 'mas não permite acesso pela posição'}
print(set)
dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'} # dicionários dict, é mutável, pode ser adicionado nos valores,
# Para acessar um valor em um dicionário, basta digitar: nome_dicionario[chave],
# E, para atribuir um novo valor, use: nome_dicionario[chave] = novo_valor