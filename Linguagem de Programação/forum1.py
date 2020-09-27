# v: 1.02
colec = []
p = ['Inventário da Coleção', ' 1 - Adicionar item: ', ' 2 - Remover item: ', ' 3 - Exibir Coleção: ', ' 4 - Sair do inventário: ', ' Opção: ', ' Inventário está vazio.', ' Opção invalida!']
i = 0
while True:
    print('', 30*'=', '\n |{:^28}|\n'.format(p[0]), 30*'=', '\n |{:<28}|\n |{:<28}|\n |{:<28}|\n |{:<28}|\n'.format(p[1], p[2], p[3], p[4]), 30*'=')
    op = int(input(p[5]))
    if op == 1:
        add = input(p[1])
        colec.append(add)
        print(' Item {} adicionado.'.format(add))
    elif op == 2:
        rem = input(p[2])
        colec.remove(rem)
        print(' Item {} removido.'.format(rem))
    elif op == 3:
        print(f'{p[3]}')
        for i in range(len(colec)):
            print(f' Item {i + 1}: {colec[i]}')
            i = i + 1
        if colec == []:
            print(p[6])
    elif op == 4:
        break
    else:
        print(p[7])
