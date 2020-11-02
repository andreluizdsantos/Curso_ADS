from typing import List


def buscar_Animais(lista, numero):
    minimo = 0
    maximo = len(lista) - 1
    encontrado = False

    while minimo <= maximo and not encontrado:
        meiodalista = (minimo + maximo) // 2
        if lista[meiodalista][0] == numero:
            encontrado = True
        else:
            if numero < lista[meiodalista][0]:
                maximo = meiodalista - 1
                print(lista[meiodalista][0])
            else:
                minimo = meiodalista + 1
                print(lista[meiodalista][0])
    return encontrado


rebanho = ['Vaca1', 'Vaca2', 'Vaca3']
reb = list(enumerate(rebanho))
num = int(input(' Digite o numero do animal: '))
num -= 1
print(buscar_Animais(reb, num))

enc = buscar_Animais(reb, num)
if enc == True:
    print(rebanho[num])
else:
    print('Não Enconctrado')
