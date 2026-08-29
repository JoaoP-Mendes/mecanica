import pymysql # importado para tratar erro
from layout import cadastrado, carregando, excluido, atualizado


class Veiculo():
    def __init__(self, conexao, cpf_cliente, placa, ano, km_atual, marca):
        self.conexao = conexao
        self.cpf_cliente = cpf_cliente
        self.placa = placa 
        self.ano = ano 
        self.km_atual = km_atual
        self.marca = marca

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, valor):
        tamanho = len(valor)
        if tamanho < 7:
            raise ValueError("Placa invalida, a placa deve conter 7 caracteres")
        elif tamanho > 7:
            raise ValueError("Placa invalida, a placa deve conter 7 caracteres")
        else:
            self._placa = valor

    @property
    def cpf_cliente(self):
        return self._cpf_cliente

    @cpf_cliente.setter
    def cpf_cliente(self, valor):
        tamanho = len(valor)
        if tamanho < 11:
            raise ValueError("CPF invalido, possui menos de 11 caracteres")
        elif tamanho > 11:
            raise ValueError("CPF invalido, possui mais de 11 caracteres")
        else:
            self._cpf_cliente = valor


    def novoVeiculo(self):
        """Metodo que realiza o cadastro de um novo veiculo, deve ser declarado o objeto para depois a comunicação com o banco"""
        try:
            inserindo = "INSERT INTO veiculo (cpf_cliente, placa, ano, km_atual, marca) VALUES (%s, %s, %s, %s, %s)"
            self.conexao.executar(inserindo, (self.cpf_cliente, self.placa, self.ano, self.km_atual, self.marca))
            cadastrado()
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")


    @staticmethod
    def listarVeiculos(conexao):
        """Metodo que lista todos os veiculos do banco de dados, retorna em uma lista, necessário infomar a conexão"""
        try:
            busca = "SELECT * FROM veiculo"
            resultado = conexao.executar(busca)
            carregando()
            return resultado
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod
    def buscarPorPlaca(conexao, placa):
        """Metodo para realizar a busca no banco, retorna em uma lista, necessário infomar a conexão e placa"""
        try:
            busca = "SELECT * FROM veiculo WHERE placa = %s"
            resultado = conexao.executar(busca, (placa, ))
            carregando()
            return resultado
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod
    def deletarVeiculo(conexao, placa):
        """Metodo para realizar a exclusão de um veículo, necessário informar a conexão e placa"""
        try:
            deletar = "DELETE FROM veiculo WHERE placa = %s"
            conexao.executar(deletar, (placa, ))
            excluido()

        except pymysql.err.IntegrityError as e:
            print("\033[31mERRO\033[m: Veiculo possui ordem em aberto(ou em andamento), exclua a ordem e trabalho para remover o veículo")
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod
    def atualizarVeiculo(conexao, tabela, novo, onde):
        """Método para realizar atualização de informação do veículo, necessário informar conexão, tabela, nova informação e placa para alteração"""
        try:
            atualizar = f"UPDATE veiculo SET {tabela} = %s WHERE placa = %s"
            conexao.executar(atualizar, (novo, onde))
            atualizado()
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")
        