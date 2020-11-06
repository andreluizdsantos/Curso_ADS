import sqlite3 #Importa a bibliotéca sqlite3


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


desc = ["Código", "Espécie", "Raça", "Data Nasc.",
        "Data Vacin.", "Ordenha", "Temp. Leite",
        "Prod. Quarto", "Prod Diária", "Ruminação", "Inseminação",
        "Estim. Parto", "Secagem"] #Adicionando valors iniciais as listas
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
    op = int(input('Digite uma opção: '))
    if op == 1:
        lista[0] = str(input('Espécie: '))
        lista[1] = str(input('Raça: '))
        lista[2] = str(input('Data Nascimento: '))
        lista[3] = str(input('Data Vacinação: '))
        print(lista)
        sql = "insert into prodLeite(esp, rac, nas, vac) values (?, ?, ?, ?)"
        #Objeto sql recebe comando para inserir os dados, e ? aponta para a posição do conteudo da lista
        cursor.execute(sql, lista)
        #O cursor executa o conteudo do objeto sql, e usa a lista para preecher os valores
        print("...dados inseridos com sucesso!")
        conector.commit()
        #Conector executado commit gravando os dados no banco
    elif op == 2:
        sql = "select * from prodLeite"
        cursor.execute(sql)
        print('Cadastrar Produção:')
        lista0[5] = int(input(' Digite o numero do animal: '))
        lista0[0] = str(input(' Horário Ordenha: '))
        lista0[1] = float(input(' Temperatura Leite: '))
        lista0[2] = float(input(' Produção Quarto: '))
        lista0[3] = lista0[2] * 4 #Calcula a produção dia
        lista0[4] = str(input('Tempo de Ruminação: '))
        print(lista0)
        sql = "UPDATE prodLeite SET ord = ?, tmp = ?, pdq = ?, pdd = ?, rum = ? WHERE (id = ?);"
        # Objeto sql recebe comando para atualizar os dados, e ? aponta para a posição do conteudo da lista
        cursor.execute(sql, lista0)
        print("...dados inseridos com sucesso!")
        conector.commit()
    elif op == 3:
        print('Cadastrar Reprodução:')
        lista[3] = int(input(' Digite o numero do animal: '))
        lista[0] = str(input('Inseminação: '))
        lista[1] = str(input('Estimativa Parto: '))
        lista[2] = str(input('Data Secagem: '))
        print(lista)
        sql = "UPDATE prodLeite SET ins = ?, ept = ?, sec = ? WHERE (id = ?);"
        cursor.execute(sql, lista)
        print("...dados inseridos com sucesso!")
        conector.commit()
    elif op == 4:
        sql = "select * from prodLeite"
        cursor.execute(sql)
        dados = cursor.fetchall()
        print("Dados da tabela 'prodLeite'")
        print(f"{len(dados)} registros Encontrados")
        num = int(input(' Digite o numero do animal: '))
        enc = buscar_Animais(dados, num) #Executa a busca binária
        if enc == True:
            print(f'Animal Encontrado:')
            for i in range(len(dados[num - 1])):
                print(f"\033[1;30;46m{desc[i]:>15}: {dados[num - 1][i]:<15}\033[m")
        else:
            print(' Não Encontrado:')
    elif op == 5:
        sql = "select * from prodLeite"
        cursor.execute(sql)
        dados = cursor.fetchall()
        print("Dados da tabela 'prodLeite'")
        print(f"{len(dados)} registros Encontrados")
        print("-" * 33)
        print("- " * 17)
        for d in dados: #Percorre todos os endereços da lista
            for i in range(len(d)):
                print(f"\033[1;30;46m{desc[i]:>15}: {d[i]:<15}\033[m")
            print("-" * 33)
    elif op == 6:
        sql = "drop table if exists prodLeite"
        #objeto sql recebe comando para excluir a tabela caso exista
        cursor.execute(sql)
        sql = "create table if not exists prodLeite(" \
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
        print('Tabela cadastro excluida e recriada')
    elif op == 9:
        break
    else:
        print('Opção inválida!')

cursor.close() #fecha o cursor
conector.close() #desconecta o banco
print("\nFim do programa")

