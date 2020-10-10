"""class PrimeiraClasse:
    nome = None

    def imprimir_mensagem(self):
        print("Olá seja bem vindo!")


objeto1 = PrimeiraClasse()
objeto1.nome = "Aluno 1"

print(objeto1.nome)
objeto1.imprimir_mensagem()
"""

"""class FuncionarioTecnico:
    def __init__(self, status):
        self.nivel = 'Técnico'
        self.status = status


func1 = FuncionarioTecnico('Ativo')
func2 = FuncionarioTecnico('Licença Mestrado')

print(func1.nivel)
print(func2.nivel)
print(func1.status)
print(func2.status)
"""

import sqlite3


class CrudSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco + '.db'

    def _conectar(self):
        conn = sqlite3.connect(self.nome_banco)
        return conn

    def criar_tabela(self, tabela, colunas): #Função recebe nome da tabela e uma lista com os dados das colunas e seus atributos
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"CREATE TABLE IF NOT EXISTS {tabela} {colunas}"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Tabela criada com sucesso!")
        return None

    def inserir_registro(self, tabela, registro): #Função recebe nome da tabela e um dicionário com os registros
        colunas = tuple(registro.keys())
        valores = tuple(registro.values())

        conn = self._conectar()
        cursor = conn.cursor()
        query = f"INSERT INTO {tabela} {colunas} VALUES {valores}"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Dados inseridos com sucesso!")
        return None

    def ler_registros(self, tabela): #Função recebe nome da tabela a ser lida
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"SELECT * FROM {tabela}"
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado

    def atualizar_registro(self, tabela, dado, condicao): #Função recebe nome da tabela, um dicionário com os dados, e um dicionário com a condição
        campo_alterar = list(dado.keys())[0]
        valor_alterar = dado.get(campo_alterar)
        campo_condicao = list(condicao.keys())[0]
        valor_condicao = condicao.get(campo_condicao)

        conn = self._conectar()
        cursor = conn.cursor()
        query = f"UPDATE {tabela} SET {campo_alterar} = '{valor_alterar}' WHERE {campo_condicao} = {valor_condicao}"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Dado atualizado com sucesso!")
        return None

    def apagar_registro(self, tabela, condicao): #Função recebe nome da tabela e um dicionário com a condição
        campo_condicao = list(condicao.keys())[0]
        valor_condicao = condicao.get(campo_condicao)
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"DELETE FROM {tabela} WHERE {campo_condicao} = {valor_condicao}"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Dado excluído com sucesso!")
        return None


"""teste = CrudSQLite('teste1')  #Objeto teste instanciado com a classe CrudSQLite()
tab = 'Cadastro'
colun = '(cod integer primary key autoincrement, nome varchar(30), tel varchar(10))'
#teste.criar_tabela(tab, colun) #Objeto teste chama a função criar_tabela()
reg = {'nome': 'André', 'tel': '9999-9999'}
#teste.inserir_registro(tab, reg) #Objeto teste chama a função inserir_registro()
cond = {'cod': 3}
teste.apagar_registro(tab, cond)  #Objeto teste chama a função apagar_registro()
dados = teste.ler_registros(tab)  #Objeto dados recebe o retorno da função teste.ler_registros()
print(f'Dados da Tabela {tab}: {dados}')
"""