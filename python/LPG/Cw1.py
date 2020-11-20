"""
def busca_sequencial(lista, elemento):
    pos = 0
    encontrado = False
    while pos < len(lista) and not encontrado:
        if lista[pos] == elemento:
            encontrado = True
        else:
            pos = pos + 1
    return encontrado
testelista = [2, 10, 8, 15, 18, 20, 12, 1]
print(busca_sequencial(testelista, 5))
print(busca_sequencial(testelista, 15))


def busca_sequencial_ordenada(lista, elemento):
    pos = 0
    encontrado = False
    para = False
    while pos < len(lista) and not encontrado and not para:
        if lista[pos] == elemento:
            encontrado = True
        else:
            if lista[pos] > elemento:
                para = True
            else:
                pos = pos + 1
    return encontrado

testelista = [1, 2, 8, 10, 13, 15, 18, 20]
print(busca_sequencial_ordenada(testelista, 5))
print(busca_sequencial_ordenada(testelista, 15))
"""
animais = [(1, 'Vaca', 'Holadesa'), (2, 'Vaca', 'Nelore'), (3, 'Vaca', 'Jersey')]

def busca_bin(lista, elem):
    min = 0
    max = len(lista) - 1
    encont = False

    while min <= max and not encont:
        meio = (min + max) // 2
        if lista[meio][0] == elem:
            encont = True
        else:
            if elem < lista[meio][0]:
                max = meio - 1
            else:
                min = meio + 1
    return encont

n = int(input('Entre com o numero do animal: '))
e = busca_bin(animais, n)

if e == True:
    print('Encontrado: ', animais[n - 1])
else:
    print(' Não Encontrado:')
