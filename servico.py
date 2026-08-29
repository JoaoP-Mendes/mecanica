from layout import cadastrado, carregando, excluido, atualizado

class Servico():
    def __init__(self, conexao, servico, valor):
        self.conexao = conexao
        self.servico = servico
        self.valor = valor


    def novoServico(self):
        """Metodo que realiza o cadastro de um novo serviço/produto, deve ser declarado o objeto para depois a comunicação com o banco"""
        try:
            inserindo = "INSERT INTO servico ( servico, valor) VALUES (%s, %s)"
            self.conexao.executar(inserindo, (self.servico, self.valor))
            cadastrado()
       
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def listarServicos(conexao):
        """Metodo que lista todos os serviço/produtos do banco de dados, retorna em uma lista, necessário infomar a conexão"""
        try:
            busca = "SELECT * FROM servico"
            resultado = conexao.executar(busca)
            carregando()
            return resultado
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def buscarPorId(conexao, id):
        """Metodo que realiza a busca do serviço/produto no banco de dados, retorna em uma lista, necessário infomar a conexão e id"""

        try:
            busca = "SELECT * FRROM servico WHERE id = %s"
            resultado = conexao.executar(busca,(id,))
            carregando()
            return resultado
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def deletarServico(conexao, id):
        """Metodo para realizar a exclusão de um serviço/produto, necessário informar a conexão e id"""

        try:
            deletar = "DELETE FROM servico WHERE id = %s"
            conexao.executar(deletar, (id,))
            excluido()
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def atualizarServico(conexao, tabela, novo, onde):
        """Método para realizar atualização dos dados do serviço/produto, necessário informar conexão, a tabela, nova informação e ID para alteração"""

        try:
            atulizar = f"UPDATE servico SET {tabela} = %s WHERE id = %s"
            conexao.executar(atulizar, (novo, onde))
            atualizado()
        except Exception as e:
            print(f"An error occured: {e}")

