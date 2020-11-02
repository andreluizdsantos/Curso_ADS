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


rebanho = []
p = ['Produção de Leite', ' 1 - Cadastrar Animal: ', ' 2 - Remover Animal: ', ' 3 - Buscar Animal: ', ' 4 - Listar Animais: ', ' 5 - Sair: ']

while True:
    print('', 30*'=', f'\n |{p[0]:^28}|\n', 30*'=', f'\n |{p[1]:<28}|\n |{p[2]:<28}|\n |{p[3]:<28}|\n |{p[4]:<28}|\n |{p[5]:<28}|\n', 30*'=')
    op = int(input(' Opção: '))
    if op == 1:
        add = input(p[1]).split()
        rebanho.append(add)
        print(f' Animal {add} adicionado.')
    elif op == 2:
        rem = int(input(p[2]))
        rem -= 1
        print(f' Animal {rebanho[rem]} removido.')
        del rebanho[rem]
    elif op == 3:
        reb = list(enumerate(rebanho))
        num = int(input(' Digite o numero do animal: '))
        num -= 1
        enc = buscar_Animais(reb, num)
        if enc == True:
            print(' Animal encontrado: ', rebanho[num])
        else:
            print(' Não Enconctrado')
    elif op == 4:
        print(f'{p[4]}')
        for i in range(len(rebanho)):
            print(f' Animal {i + 1}: ', rebanho[i])
        if rebanho == []:
            print(' Nenhum Animal Registrado.')
    elif op == 5:
        break
    else:
        print(' Opção invalida!')
