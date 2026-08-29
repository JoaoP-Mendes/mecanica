import pymysql # importado para tratar erro
from layout import cadastrado, carregando, excluido, atualizado


class Cliente():
    def __init__(self, conexao, cpf, nome, data_nascimento, telefone, ativo):
        self.conexao = conexao
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.nome = nome
        self.telefone = telefone
        self.ativo = ativo

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        tamanho = len(valor)
        if tamanho < 11:
            raise ValueError("CPF invalido, possui menos de 11 caracteres")
        elif tamanho > 11:
            raise ValueError("CPF invalido, possui mais de 11 caracteres")
        else:
            self._cpf = valor


    def novoCliente(self):
        """Realiza o envio de um novo cliente para o banco de dados"""
        try:
            inserindo = "INSERT INTO cliente (cpf, nome, data_nascimento, telefone, ativo_sn) VALUES (%s, %s, %s, %s, %s)"
            self.conexao.executar(inserindo, (self.cpf, self.nome, self. data_nascimento, self.telefone, self.ativo))
            cadastrado()
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod #Define como método não uma instancia, ou seja, não é necessário o self
    def listarClientes(conexao):
        try:
            buscar = "SELECT * FROM cliente"
            resultado = conexao.executar(buscar)
            carregando()
            return resultado
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod
    def buscarPorCpf(conexao, valor):
        try:
            buscar = "SELECT * FROM cliente WHERE cpf = %s"
            resultado = conexao.executar(buscar, (valor,))
            carregando()
            return resultado
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod
    def deletarCliente(conexao, valor):
        try:
            deletar = "DELETE FROM cliente WHERE cpf = %s"
            conexao.executar(deletar, (valor,))
            excluido()
        except pymysql.err.IntegrityError as e:
            print(f"ERRO: Ação não realizada, será necessário remover o veículo do cliente primeiro")
            print("")
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")

    @staticmethod
    def atualizarCliente(conexao, tabela, novo, onde):
        try:
            atualizar = f"UPDATE cliente SET {tabela} = %s WHERE cpf = %s"
            conexao.executar(atualizar, (novo, onde))
            atualizado()
        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")