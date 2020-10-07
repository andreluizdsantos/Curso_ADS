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

    def inserir_registro(self, tabela, registro):
        colunas = tuple(registro.keys())
        valores = tuple(registro.values())

        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""INSERT INTO {tabela} {colunas} VALUES {valores}"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Dados inseridos com sucesso!")
        return None

    def ler_registros(self, tabela):
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""SELECT * FROM {tabela}"""
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado

    def atualizar_registro(self, tabela, dado, condicao):
        campo_alterar = list(dado.keys())[0]
        valor_alterar = dado.get(campo_alterar)
        campo_condicao = list(condicao.keys())[0]
        valor_condicao = condicao.get(campo_condicao)

        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""UPDATE {tabela} SET {campo_alterar} = '{valor_alterar}' WHERE {campo_condicao} = {valor_condicao}"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Dado atualizado com sucesso!")
        return None

    def apagar_registro(self, tabela, condicao):
        campo_condicao = list(condicao.keys())[0]
        valor_condicao = condicao.get(campo_condicao)
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""DELETE FROM {tabela} WHERE {campo_condicao} = {valor_condicao}"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Dado excluído com sucesso!")
        return None

while True:
    print('Criando e manipulando banco de dados')
    print(' 1 - Criar Banco de dados:\n 2 - Inserir dados:\n 3 - Ler dados:\n 4 - Remover dados:\n 5 - Sair: ')
    op = int(input('Digite uma Opção: '))
    if op == 1:
        nome = input('Digite o nome do Banco de dados: ')
        CrudSQLite(nome)
    elif op == 2:
        tabela = input('Digite o nome da tabela: ')
        regitro = input('Digite o valor a ser registrado')
        nome._conectar(nome)
        nome.inserir_registro()
    elif op == 5:
        break