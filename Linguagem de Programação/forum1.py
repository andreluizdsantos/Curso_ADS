# v: 1.01
colec = []
nome = 'Inventário da Coleção'
adic = ' 1 - Adicionar item: '
remo = ' 2 - Remover item: '
exib = ' 3 - Exibir Coleção: '
sair = ' 4 - Sair do inventário: '

while True:
    print('', 30*'=', '\n |{:^28}|\n'.format(nome), 30*'=', '\n |{:<28}|\n |{:<28}|\n |{:<28}|\n |{:<28}|\n'.format(adic, remo, exib, sair), 30*'=')
    op = int(input(' Opção: '))
    if op == 1:
        add = input(adic)
        colec.append(add)
        print(' Item {} adicionado.'.format(add))
    elif op == 2:
        rem = input(remo)
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
