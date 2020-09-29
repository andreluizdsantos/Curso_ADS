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

aluno = dict()
aluno['nome'] = str(input('Digite seu nome: '))
aluno['media'] = float(input('Digite sua média: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
for x, y in aluno.items():
    print(f'- {x} é igual a {y}')
print(aluno.keys())
print(aluno.values)