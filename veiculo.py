from banco import BancoDados

connObj = BancoDados()
connObj.conectar()


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
        """Realiza o cadastro de um novo veiculo, deve ser declarado o objeto para depois a comunicação com o banco"""
        try:
            inserindo = "INSERT INTO veiculo (cpf_cliente, placa, ano, km_atual, marca) VALUES (%s, %s, %s, %s, %s)"
            self.conexao.executar(inserindo, (self.cpf_cliente, self.placa, self.ano, self.km_atual, self.marca))
            print("Cadastrado")
        except Exception as e:
            print(f"An error occured: {e}")


    @staticmethod
    def listarVeiculos(conexao):
        try:
            busca = "SELECT * FROM veiculo"
            resultado = conexao.executar(busca)
            return resultado
        except Exception as e:
            print(f"An error occured")

    @staticmethod
    def buscarPorPlaca(conexao, placa):
        try:
            busca = "SELECT * FROM veiculo WHERE placa = %s"
            resultado = conexao.executar(busca, (placa, ))
            return resultado
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def deletarVeiculo(conexao, placa):
        try:
            deletar = "DELETE FROM veiculo WHERE placa = %s"
            conexao.executar(deletar, (placa, ))
            print("Exclusão realizada")
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def atualizarCliente(conexao, tabela, novo, onde):
        try:
            atualizar = f"UPDATE veiculo SET {tabela} = %s WHERE placa = %s"
            conexao.executar(atualizar, (novo, onde))
        except Exception as e:
            print(f"An error occured: {e}")
        

"""cpf_cliente = input("Digite o cpf: ")
placa = input("Digite a placa: ")
ano = input("Ano do carro: ")
km_atual = input("Quilometragem do carro: ")
marca = input("Qual a marca? ")

carro = Veiculo(connObj, cpf_cliente, placa, ano, km_atual, marca)
carro.novoVeiculo()
"""
# busca = Veiculo.listarVeiculos(connObj)
# for cada in busca:
#     print(cada)


# busca = Veiculo.buscarPorPlaca(connObj, 'zxcv123')
# for i in busca:
#     print(i)

# placa = input("Informe o CPF para exclusao: ")
# Veiculo.deletarVeiculo(connObj, placa)