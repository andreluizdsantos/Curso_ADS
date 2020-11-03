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
            else:
                minimo = meiodalista + 1
    return encontrado
