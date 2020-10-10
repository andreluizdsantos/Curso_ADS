# v: 1.04
colec = []
p = ['Inventário da Coleção', ' 1 - Adicionar item: ', ' 2 - Remover item: ', ' 3 - Exibir Coleção: ', ' 4 - Sair do inventário: ', ' Opção: ', ' Inventário está vazio.', ' Opção invalida!']
i = 0
while True:
    print('', 30*'=', f'\n |{p[0]:^28}|\n', 30*'=', f'\n |{p[1]:<28}|\n |{p[2]:<28}|\n |{p[3]:<28}|\n |{p[4]:<28}|\n', 30*'=')
    op = int(input(p[5]))
    if op == 1:
        add = input(p[1])
        colec.append(add)
        print(f' Item {add} adicionado.')
    elif op == 2:
        rem = input(p[2])
        colec.remove(rem)
        print(f' Item {rem} removido.')
    elif op == 3:
        print(f'{p[3]}')
        for i in range(len(colec)):
            print(f' Item {i + 1}: {colec[i]}')
        if colec == []:
            print(p[6])
    elif op == 4:
        break
    else:
        print(p[7])
