import Cw3 as C

teste = C.CrudSQLite('teste1')  #Objeto teste instanciado com a classe CrudSQLite()
tab = 'Cadastro'
colun = '(cod integer primary key autoincrement, nome varchar(30), tel varchar(10))'
#teste.criar_tabela(tab, colun) #Objeto teste chama a função criar_tabela()
reg = {'nome': 'Joice', 'tel': '9999-9998'}
#teste.inserir_registro(tab, reg) #Objeto teste chama a função inserir_registro()
cond = {'cod': 3}
#teste.apagar_registro(tab, cond)  #Objeto teste chama a função apagar_registro()
dados = teste.ler_registros(tab)  #Objeto dados recebe o retorno da função teste.ler_registros()
print(f'Dados da Tabela {tab}: {dados}')