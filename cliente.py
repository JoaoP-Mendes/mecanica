from banco import BancoDados

connObj = BancoDados()
connObj.conectar()

class Cliente():
    def __init__(self, conexao, cpf, nome, data_nascimento, telefone, ativo):
        self.conexao = conexao
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
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
            self.conexao.executar(inserindo, (self.cpf, self.nome, self.data_nascimento, self.telefone, self.ativo))
            print("Cadastrado")
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod #Define como método não uma instancia, ou seja, não é necessário o self
    def listarClientes(conexao):
        try:
            buscar = "SELECT * FROM cliente"
            resultado = conexao.executar(buscar)
            return resultado
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def buscarPorCpf(conexao, valor):
        try:
            buscar = "SELECT * FROM cliente WHERE cpf = %s"
            resultado = conexao.executar(buscar, (valor,))
            return resultado
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def deletarCliente(conexao, valor):
        try:
            deletar = "DELETE FROM cliente WHERE cpf = %s"
            conexao.executar(deletar, (valor,))
            print("Exclusão realizada\n")
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def atualizarCliente(conexao, tabela, novo, onde):
        try:
            atualizar = f"UPDATE cliente SET {tabela} = %s WHERE cpf = %s"
            conexao.executar(atualizar, (novo, onde))
        except Exception as e:
            print(f"An error occured: {e}")



"""cpf = input("Digite o CPF: ")
nome = input("Digite o nome: ")
data_nascimento = input("Data nascimento: ")
telefone = input("Qual o telefone: ")
ativo = input("Está ativo? S/N ").upper()

cliente = Cliente(connObj, cpf, nome, data_nascimento, telefone, ativo)
cliente.novoCliente()"""

#retorno = Cliente.listarClientes(connObj)
#for r in retorno:
#    print(r)

# retorno = Cliente.buscarPorCpf(connObj, 12345678911)
# for i in retorno:
#     print(i)

# cpfcliente = input("Informe o cpf para exclusão: ")
# cpfexclusao = Cliente.deletarCliente(connObj, cpfcliente)

# tabelas = {'ativo_sn'}
# oqueatualizar = input("O que atualizar? ")
# if oqueatualizar in tabelas: 
#     novainfo = input("Digite a nova info: ")
#     dequem = input("De quem? ")
#     Cliente.atualizarCliente(connObj, oqueatualizar, novainfo, dequem)




"""class Pessoa:
    def __init__(self, idade):
        self.idade = idade          # repara: chama o "porteiro" já aqui

    @property
    def idade(self):
        return self._idade           # o que acontece quando você LÊ pessoa.idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = valor          # o que acontece quando você ESCREVE pessoa.idade = valor"""