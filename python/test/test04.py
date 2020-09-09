colec = []
while True:
    print('', 29*'=', '\n === Inventário da Coleção ===\n', 29*'=', '\n 1 - Adicionar item.\n 2 - Remover item.\n 3 - Exibir Coleção.\n 4 - Sair do inventário.\n', 29*'=')
    op = int(input(' Opção: '))
    if op == 1:
        add = input(' Adicionar item: ')
        colec.append(add)
        print(' Item {} adicionado.'.format(add))
    elif op == 2:
        rem = input(' Remover item: ')
        colec.remove(rem)
        print(' Item {} removido.'.format(rem))
    elif op == 3:
        print(' Lista de itens da coleção:\n {}'.format(colec))
        if colec == []:
            print(' Inventário está vazio.')
    elif op == 4:
        break
    else:
        print(' Opção invalida!')
