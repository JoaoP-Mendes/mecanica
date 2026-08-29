from banco import BancoDados
from datetime import date

conn = BancoDados()
conn.conectar()


class ordem_Servico():
    def __init__(self,conexao, id_veiculo):
        self.conexao = conexao
        self.id_veiculo = id_veiculo
        self.data_inicio = date.today()

    def novaOrdemServico(self):
        try:    
            inserindo = "INSERT INTO ordem_servico (id_veiculo, data_inicio) VALUES (%s, %s)"
            self.conexao.executar(inserindo, (self.id_veiculo, self.data_inicio))
        except Exception as e:
            print(f"An error occured: {e}")


    @staticmethod
    def listarOrdens(conexao):
        try:
            busca = "SELECT * FROM ordem_servico"
            resultado = conexao.executar(busca)
            return resultado
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def buscarPorId(conexao, id):
        try:
            busca = "SELECT * FROM ordem_servico WHERE id = %s"
            resultado = conexao.executar(busca, (id,))
            return resultado
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def deletarOrdem(conexao, id):
        try:
            deletar = "DELETE FROM ordem_servico WHERE id = %s"
            conexao.executar(deletar, (id, ))
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod 
    def atualizarStatus(conexao, novo, onde):
        try:
            atualizar = "UPDATE ordem_servico SET status = %s WHERE id = %s"
            conexao.executar(atualizar, (novo, onde))
        except Exception as e:
            print(f"An error occured: {e}")


    @staticmethod
    def adicionarItem(conexao, id_ordem_servico, id_servico):
        try: 
            inserindo = "INSERT INTO itens_servico (id_ordem_servico, id_servico) VALUES (%s, %s)"
            conexao.executar(inserindo, (id_ordem_servico, id_servico))
        except Exception as e:
            print(f"An error occured: {e}")


    @staticmethod
    def listarItens(conexao):
        try:
            busca = "SELECT * FROM itens_servico"
            resultado = conexao.executar(busca)
            return resultado
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def deletarItem(conexa, id):
        try:
            deletar = "DELETE FROM itens_servico WHERE id = %s"
            conexa.executar(deletar(id,))
        except Exception as e:
            print(f"An error occured: {e}")


"""id_veiculo = input("Id: ")
ordem = ordem_Servico(conn, id_veiculo)
ordem.novaOrdemServico()"""


"""busca = ordem_Servico.listarOrdens(conn)
for cada in busca:
    print(cada)"""
