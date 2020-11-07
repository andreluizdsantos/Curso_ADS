import sqlite3 #Importa a biblioteca sqlite3


def buscar_Animais(lista, numero): #Cria a função de busca binária
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


desc = ["Código......", "Espécie.....", "Raça........", "Data Nasc...",
        "Data Vacin..", "Ordenha.....", "Temp. Leite.",
        "Prod. Quarto", "Prod. Diária", "Ruminação...", "Inseminação.",
        "Estim. Parto", "Secagem....."] #Adicionando valores iniciais as listas
lista = ['', '', '', '']
lista0 = ['', '', '', '', '', '']

conector = sqlite3.connect('fazentech.db') #Conecta o banco de dados
cursor = conector.cursor() #Iniciando o cursor

while True:
    print(f"\n\033[1;30;46m #FAZENTECH \033[m\nBanco de Dados 'fazentech.db'")
    print('\033[1;30;41m  *CRUD* Teste - Busca Binária  \033[m')
    print("""    1 - Cadastrar Animal:
    2 - Cadastro Produção:
    3 - Cadastro Reprodução:
    4 - Busca Binária:
    5 - Consulta Tabela:
    6 - Excluir/Criar Tabela:
    7 - Sair""")
    op = int(input(' Digite uma Opção: '))
    if op == 1:
        lista[0] = str(input('Espécie: '))
        lista[1] = str(input('Raça: '))
        lista[2] = str(input('Data Nascimento: '))
        lista[3] = str(input('Data Vacinação: '))
        print(lista)
        sql = "INSERT INTO prodLeite(esp, rac, nas, vac, ord, tmp," \
              " pdq, pdd, rum, ins, ept, sec)" \
              " VALUES (?, ?, ?, ?, '', '', '', '', '', '', '', '')"
        #Objeto sql recebe comando para inserir os dados, e ? aponta para a posição do conteudo da lista
        cursor.execute(sql, lista)
        #O cursor executa o conteudo do objeto sql, e usa a lista para preencher os valores
        print(" ...Dados Inseridos com Sucesso!")
        conector.commit()
        #Conector executado commit gravando os dados no banco
    elif op == 2:
        sql = "SELECT * FROM prodLeite"
        cursor.execute(sql)
        print(' Cadastrar Produção:')
        lista0[5] = int(input(' Digite o Número do Animal: '))
        lista0[0] = str(input(' Horário Ordenha: '))
        lista0[1] = float(input(' Temperatura Leite: '))
        lista0[2] = float(input(' Produção Quarto: '))
        lista0[3] = lista0[2] * 4 #Calcula a produção dia
        lista0[4] = str(input(' Tempo de Ruminação: '))
        print(lista0)
        sql = "UPDATE prodLeite SET ord = ?, tmp = ?, pdq = ?, pdd = ?, rum = ? WHERE (id = ?);"
        # Objeto sql recebe comando para atualizar os dados, e ? aponta para a posição do conteúdo da lista
        cursor.execute(sql, lista0)
        print(" ...Dados Inseridos com Sucesso!")
        conector.commit()
    elif op == 3:
        print(' Cadastrar Reprodução:')
        lista[3] = int(input(' Digite o Número do Animal: '))
        lista[0] = str(input(' Inseminação: '))
        lista[1] = str(input(' Estimativa Parto: '))
        lista[2] = str(input(' Data Secagem: '))
        print(lista)
        sql = "UPDATE prodLeite SET ins = ?, ept = ?, sec = ? WHERE (id = ?);"
        cursor.execute(sql, lista)
        print(" ...Dados Inseridos com Sucesso!")
        conector.commit()
    elif op == 4:
        sql = "SELECT * FROM prodLeite"
        cursor.execute(sql)
        dados = cursor.fetchall()
        print(" Dados da Tabela 'prodLeite'")
        print(f'\033[1;30;42m{len(dados):5} Registros Encontrados', ' ' * 3, '\033[m')
        num = int(input(' Digite o número do Animal: '))
        enc = buscar_Animais(dados, num) #Executa a busca binária
        if enc == True:
            print('\033[1;30;42m', ' '*5, 'Animal Encontrado:', ' '*5, '\033[m')
            for i in range(len(dados[num - 1])):
                print(f"\033[1;30;46m{desc[i]:>15}: {dados[num - 1][i]:<15}\033[m")
        else:
            print('\033[1;30;41m', ' '*3, 'Animal Não Encontrado:', ' '*3, '\033[m')
    elif op == 5:
        sql = "SELECT * FROM prodLeite"
        cursor.execute(sql)
        dados = cursor.fetchall()
        print(" Dados da tabela 'prodLeite'")
        print(f'\033[1;30;42m{len(dados):5} Registros Encontrados', ' ' * 3, '\033[m')
        print("-" * 32)
        for d in dados: #Percorre todos os endereços da lista
            for i in range(len(d)):
                print(f"\033[1;30;46m{desc[i]:>15}: {d[i]:<15}\033[m")
            print("-" * 32)
    elif op == 6:
        sql = "DROP TABLE IF EXISTS prodLeite"
        #objeto sql recebe comando para excluir a tabela caso exista
        cursor.execute(sql)
        sql = "CREAT TABLE IF NOT EXISTS prodLeite(" \
              "id integer primary key autoincrement," \
              " esp varchar(20)," \
              " rac varchar(20)," \
              " nas DATE," \
              " vac DATE," \
              " ord TIME," \
              " tmp FLOAT," \
              " pdq FLOAT," \
              " pdd FLOAT," \
              " rum TIME," \
              " ins ENUM," \
              " ept DATE," \
              " sec DATE)"
        #objeto sql recebe comando para cria tabela
        cursor.execute(sql)
        print(' Tabela prodLeite Excluída e Recriada')
    elif op == 7:
        break
    else:
        print(' Opção Inválida!')

cursor.close() #fecha o cursor
conector.close() #desconecta o banco
print('\n\033[1;30;41m', ' ' * 6, 'Fim do Programa!', ' ' * 6, '\033[m')
