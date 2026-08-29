from banco import BancoDados
from cliente import Cliente

connObj = BancoDados()
connObj.conectar()

def menu_cliente(connObj):
    while True:
        try:
            resposta = int(input("\033[36m----- MENU CLIENTE -----\033[m\n1 - Adicionar usuário \n2 - Listar \n3 - Buscar por CPF \n4 - Atualizar cliente \n5 - Deletar cliente \n0 - Voltar para o menu\nResposta: "))
            if resposta == 1:
                print("")
                cpf = input("\033[4mDigite o CPF\033[m: ") 
                nome = input("\033[4mDigite o nome:\033[m ")
                data_nascimento = input("\033[4mData nascimento:\033[m ")
                telefone = input("\033[4mQual o telefone:\033[m ")
                ativo = input("\033[4mEstá ativo? S/N\033[m ").upper()

                cliente = Cliente(connObj, cpf, nome,data_nascimento, telefone, ativo)
                cliente.novoCliente()

            elif resposta == 2: 
                print("")
                lista_clientes = Cliente.listarClientes(connObj)
                print("CADASTRADO CLIENTES: ")
                for cada_cliente in lista_clientes:
                    print(cada_cliente)
                print("")

            elif resposta == 3:
                print("")
                cpf_busca = input("Informe o CPF para busca: ")
                resultado = Cliente.buscarPorCpf(connObj, cpf_busca)
                print("RESULTADO BUSCA: ")
                print(resultado)
                print("")

            elif resposta == 4:
                tabelas = {'nome', 'nome', 'data_nascimento', 'telefone', 'ativo_sn'}
                print("")
                o_que_atualizar = input("Qual informação gostaria de atualizar? ")
                if o_que_atualizar in tabelas:
                    nova_info = input("Digite a nova informação: ")
                    qual_cpf = input("Digite o CPF do cliente para confirmação: ")
                    Cliente.atualizarCliente(connObj, o_que_atualizar, nova_info, qual_cpf)

            elif resposta == 5:
                print("")
                cpf_exclusao = input("Informe o CPF para exclusão: ")
                Cliente.deletarCliente(connObj, cpf_exclusao)

            elif resposta == 0:
                print("")
                print("Voltando para para o menu inical")
                print("")

            else:
                print("")
                print("\033[31mERRO\033[m: Ação não reconhecida, informe uma ação valida")
                print("")
                continue
        except Exception as e:
            print(f"An error occured: {e}")


menu_cliente(connObj)

# \033[4m Texto \033[m -> sublinhado 
