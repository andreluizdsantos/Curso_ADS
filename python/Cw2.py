"""def ValorLista():
    for i in range(1,5):
        lista.append(int(input(f'Digite o valor da sua {i} prova: ')))

def Media():
    s = 0
    for i in range(len(lista)):
        s = s + lista[i]
    m = s / 4
    return m

lista =[]
ValorLista()
m = Media()
print(f'O valor da sua média é: {m}')"""

"""aluno = dict()
aluno['nome'] = str(input('Digite seu nome: '))
aluno['media'] = float(input('Digite sua média: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
for x, y in aluno.items():
    print(f'- {x} é igual a {y}')
print(aluno.keys())
print(aluno.values)"""

def busca_sec(lista, elem):
    pos = 0
    enc = False
    while pos < len(lista) and not enc:
        if elem == lista[pos]:
            enc = True
        else:
            pos = pos +1
    return enc

lista1 = list(range(0, 20, 3))
a = busca_sec(lista1, 3)
b = busca_sec(lista1, 10)
print(f'Lista: {lista1}\nTeste1 busca numero 3: {a},\nTeste2 busca numero 10: {b}')