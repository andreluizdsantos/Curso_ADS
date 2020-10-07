import sqlite3

desc = ["Código", "Nome", "Telefone"]
lista = [None, None]
menu = [' 1 - Cadastrar:', ' 2 - Consultar:', ' 3 - Excluir/Criar Tabela:', ' 9 - Sair e Salvar']
conector = sqlite3.connect('teste.db')
cursor = conector.cursor()

while True:
    print(f"*CRUD* Teste\nBanco de Dados 'teste.db'\n{menu[0]}\n{menu[1]}\n{menu[2]}\n{menu[3]}")
    op = int(input('Digite uma opção: '))
    if op == 1:
        lista[0] = str(input('Digite o nome: '))
        lista[1] = str(input('Digite o telefone: '))
        print(lista)
        sql = "insert into cadastro (nome, tel) values (?, ?)"  # ? aponta para a posição da lista
        cursor.execute(sql, lista)
        print(" "*3,"...dados inseridos com sucesso")
    elif op == 2:
        sql = "select * from cadastro"  # Lista os dados no banco
        cursor.execute(sql)
        dados = cursor.fetchall()
        print("Dados da tabela 'cadastro'")
        print(f"{len(dados)} registros Encontrados")
        print("-" * 37)
        print(f"{desc[0]:^7} {desc[1]:^20} {desc[2]:^8}")
        print("- " * 19)
        for d in dados:
            print(f"{d[0]:^7} {d[1]:20} {d[2]:^8}")
            print("-" * 37)
    elif op == 3:
        sql = "drop table if exists cadastro" #exclui tabela caso exista
        cursor.execute(sql)
        sql = "create table if not exists cadastro (id integer primary key autoincrement, nome varchar(30), tel varchar(10))"  # cria tabela
        cursor.execute(sql)
        print('Tabela cadastro excluida e recriada')
    elif op == 9:
        conector.commit()
        break
    else:
        print('Opção inválida!')

cursor.close()
conector.close()
print("\nFim do programa")
