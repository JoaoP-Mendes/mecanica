from banco import BancoDados
from layout import cadastrado, carregando, excluido, atualizado

conn = BancoDados ()
conn.conectar()

class Servico():
    def __init__(self, conexao, servico, valor):
        self.conexao = conexao
        self.servico = servico
        self.valor = valor


    def novoServico(self):
        """Realiza o envio de um novo serviço para o banco de dados"""
        try:
            inserindo = "INSERT INTO servico ( servico, valor) VALUES (%s, %s)"
            self.conexao.executar(inserindo, (self.servico, self.valor))
            cadastrado()
       
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def listarServicos(conexao):
        try:
            busca = "SELECT * FROM servico"
            resultado = conexao.executar(busca)
            carregando()
            return resultado
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def buscarPorId(conexao, id):
        try:
            busca = "SELECT * FRROM servico WHERE id = %s"
            resultado = conexao.executar(busca,(id,))
            carregando()
            return resultado
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def deletarServico(conexao, id):
        try:
            deletar = "DELETE FROM servico WHERE id = %s"
            conexao.executar(deletar, (id,))
            excluido()
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def atualizarServico(conexao, tabela, novo, onde):
        try:
            atulizar = f"UPDATE servico SET {tabela} = %s WHERE id = %s"
            conexao.executar(atulizar, (novo, onde))
            atualizado()
        except Exception as e:
            print(f"An error occured: {e}")




# servico = input("Qual seria o servico: ")
# valor = input("Qual o valor? ")

# novo = Servico(conn, servico, valor)
# novo.novoServico()

# busca = Servico.listarServicos(conn)
# for cada in busca:
#     print(cada)

# busca = Servico.buscarPorId(conn, '1')
# for cada in busca:
#     print(cada)

# id = input("Informe o ID para exclusão: ")
# Servico.deletarServico(conn, id)