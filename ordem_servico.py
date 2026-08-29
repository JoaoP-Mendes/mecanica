from datetime import date
import pymysql # importado para tratar erro
from layout import cadastrado, carregando, excluido, atualizado


class ordem_Servico():
    def __init__(self,conexao, id_veiculo):
        self.conexao = conexao
        self.id_veiculo = id_veiculo
        self.data_inicio = date.today()

    def novaOrdemServico(self):
        """Metodo que realiza o cadastro de uma nova ordem de serviço, deve ser declarado o objeto para depois a comunicação com o banco"""

        try:    
            inserindo = "INSERT INTO ordem_servico (id_veiculo, data_inicio) VALUES (%s, %s)"
            self.conexao.executar(inserindo, (self.id_veiculo, self.data_inicio))
            cadastrado()
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod
    def listarOrdens(conexao):
        """Metodo que lista todas as ordens de serviço do banco de dados, retorna em uma lista, necessário infomar a conexão"""

        try:
            busca = "SELECT * FROM ordem_servico"
            resultado = conexao.executar(busca)
            carregando()
            return resultado
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod
    def buscarPorId(conexao, id):
        """Metodo para realizar a busca no banco, retorna em uma lista, necessário infomar a conexão e id"""
 
        try:
            busca = "SELECT * FROM ordem_servico WHERE id = %s"
            resultado = conexao.executar(busca, (id,))
            carregando()
            return resultado
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod
    def deletarOrdem(conexao, id):
        """Metodo para realizar a exclusão de uma ordem de serviço, necessário informar a conexão e id"""
        try:
            deletar = "DELETE FROM ordem_servico WHERE id = %s"
            conexao.executar(deletar, (id, ))
            excluido()
        except pymysql.err.IntegrityError as e:
            print("\033[31mERRO\033[m: Exclua o trabalho antes de prosseguir") 
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod 
    def atualizarStatus(conexao, novo, onde):
        """Metodo para realizar a atualização dos status da ordem de serviço, necessário informar conexão, tabela, nova informação e id para alteração"""
        try:
            atualizar = "UPDATE ordem_servico SET status = %s WHERE id = %s"
            conexao.executar(atualizar, (novo, onde))
            atualizado()
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")


    @staticmethod
    def adicionarItem(conexao, id_ordem_servico, id_servico):
        """Realiza o cadastro de um trabalho, não é necesário declarar um objeto antes"""
        try: 
            inserindo = "INSERT INTO itens_servico (id_ordem_servico, id_servico) VALUES (%s, %s)"
            conexao.executar(inserindo, (id_ordem_servico, id_servico))
            cadastrado()
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")


    @staticmethod
    def listarItens(conexao):
        """Metodo que lista todos os trabalhos no banco de dados, retorna em uma lista, necessário infomar a conexão"""
        try:
            busca = "SELECT * FROM itens_servico"
            resultado = conexao.executar(busca)
            carregando()
            return resultado
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod
    def deletarItem(conexa, id):
        """Metodo para realizar a exclusão de um trabalho, necessário informar a conexão e id"""
        try:
            deletar = "DELETE FROM itens_servico WHERE id = %s"
            conexa.executar(deletar(id,))
            excluido()
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")
