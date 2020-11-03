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
p = ['Produção de Leite', ' 1 - Cadastrar Vaca: ', ' 2 - Remover: ', ' 3 - Buscar: ', ' 4 - Listar: ', ' 5 - Sair: ']

while True:
    print('', 30*'=', f'\n |{p[0]:^28}|\n', 30*'=', f'\n |{p[1]:<28}|\n |{p[2]:<28}|\n |{p[3]:<28}|\n |{p[4]:<28}|\n |{p[5]:<28}|\n', 30*'=')
    op = int(input(' Opção: '))
    if op == 1:
        if rebanho == []:
            j = 1
        else:
            i = len(rebanho) - 1
            j = rebanho[i][0] + 1
        add = j, input(p[1]) #Adiciona código numérico
        rebanho.append(add)
        print(f' Animal {add} cadastrado.')
    elif op == 2:
        rem = int(input(p[2]))
        rem -= 1
        print(f' Animal {rebanho[rem]} removido.')
        del rebanho[rem]
    elif op == 3:
        num = int(input(' Digite o numero do animal: '))
        enc = buscar_Animais(rebanho, num) #Executa a busca binária
        if enc == True:
            print(' Animal Encontrado: ', rebanho[num - 1])
        else:
            print(' Não Encontrado:')
    elif op == 4:
        print(f'{p[4]}')
        for i in range(len(rebanho)):
            print(' Animal: ', rebanho[i])
        if rebanho == []:
            print(' Nenhum Animal Cadastrado.')
    elif op == 5:
        break
    else:
        print(' Opção invalida!')

