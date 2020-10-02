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