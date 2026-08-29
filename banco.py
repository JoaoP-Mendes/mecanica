import pymysql.connections
from config import DB_CONFIG

class BancoDados():
    def __init__(self):
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = pymysql.connections.Connection(**DB_CONFIG)

        except Exception as e:
            print(f"An error occured: {e}")

    def desconectar(self):
        try:
            self.conexao.close()

        except Exception as e:
            print(f"An error occured: {e}")

    def executar(self, query, valor = ()):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query, valor)

            if query.strip().upper().startswith("SELECT"):
                resultado = cursor.fetchall()
                return resultado
            else:
                self.conexao.commit()
                return cursor.lastrowid

       
        except Exception as e:
            raise


"""query = "SELECT * FROM livros WHERE id = %s"
self.conexao.executar(query, (id,))"""