from banco import BancoDados
from cliente import Cliente
from veiculo import Veiculo
from servico import Servico



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
                cpf_busca = input(" \033[4mInforme o CPF para busca:\033[m ")
                resultado = Cliente.buscarPorCpf(connObj, cpf_busca)
                print("RESULTADO BUSCA: ")
                print(resultado)
                print("")

            elif resposta == 4:
                tabelas = {'nome', 'data_nascimento', 'telefone', 'ativo_sn'}
                print("")
                o_que_atualizar = input("\033[4mQual informação gostaria de atualizar?\033[m ")
                if o_que_atualizar in tabelas:
                    nova_info = input("\033[4mDigite a nova informação: \033[m ")
                    qual_cpf = input("\033[4mDigite o CPF do cliente para confirmação: \033[m ")
                    Cliente.atualizarCliente(connObj, o_que_atualizar, nova_info, qual_cpf)

            elif resposta == 5:
                print("")
                cpf_exclusao = input("\033[4mInforme o CPF para exclusão: \033[m ")
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
            continue

def menu_veiculo(connObj):
    while True:
        try:
            resposta = int(input("\033[36m----- MENU VEICULO -----\033[m\n1 - Adicionar veiculo \n2 - Listar \n3 - Buscar por placa \n4 - Atualizar veiculo \n5 - Deletar veiculo \n0 - Voltar para o menu\nResposta: "))
            if resposta == 1:
                print("")
                cpf_cliente = input("\033[4mDigite o CPF\033[m: ") 
                placa = input("\033[4mDigite a placa:\033[m ")
                ano = input("\033[4mAno do veiculo:\033[m ")
                km_atual = input("\033[4mQuilometragem atual:\033[m ")
                marca = input("\033[4mMarca do veiculo:\033[m ").upper()

                carro = Veiculo(connObj, cpf_cliente, placa, ano, km_atual, marca)
                carro.novoVeiculo()

            elif resposta == 2: 
                print("")
                lista_veiculo = Veiculo.listarVeiculos(connObj)
                print("VEICULOS CADASTRADOS: ")
                for cada_veiculo in lista_veiculo:
                    print(cada_veiculo)
                print("")

            elif resposta == 3:
                print("")
                placa_busca = input(" \033[4mInforme a placa para busca:\033[m ")
                resultado = Veiculo.buscarPorPlaca(connObj, placa_busca)
                print("RESULTADO BUSCA: ")
                print(resultado)
                print("")

            elif resposta == 4:
                tabelas = {'cpf_cliente', 'placa', 'ano', 'km_atual', 'marca'}
                print("")
                o_que_atualizar = input("\033[4mQual informação gostaria de atualizar?\033[m ")
                if o_que_atualizar in tabelas:
                    nova_info = input("\033[4mDigite a nova informação: \033[m ")
                    qual_placa = input("\033[4mDigite a placa do veiculo para confirmação: \033[m ")
                    Veiculo.atualizarVeiculo(connObj, o_que_atualizar, nova_info, qual_placa)


            elif resposta == 5:
                print("")
                placa_exclusao = input("\033[4mInforme a Placa para exclusão: \033[m ")
                Veiculo.deletarVeiculo(connObj, placa_exclusao)

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
            continue



def menu_servico(connObj):
    while True:
        try:
            resposta = int(input("\033[36m----- MENU SERVIÇO -----\033[m\n1 - Adicionar novo serviço \n2 - Listar \n3 - Buscar por ID \n4 - Atualizar serviço \n5 - Deletar serviço \n0 - Voltar para o menu\nResposta: "))
            if resposta == 1:
                print("")
                servico = input("\033[4mDigite o serviço\033[m: ") 
                valor = input("\033[4mDigite a placa:\033[m ")

                serv = Servico(connObj, servico, valor)
                serv.novoServico()

            elif resposta == 2: 
                print("")
                lista_servico = Servico.listarServicos(connObj)
                print("SERVIÇOS CADASTRADOS: ")
                for cada_servico in lista_servico:
                    print(cada_servico)
                print("")

            elif resposta == 3:
                print("")
                id_busca = input(" \033[4mInforme o ID para busca:\033[m ")
                resultado = Servico.buscarPorId(connObj, id_busca)
                print("RESULTADO BUSCA: ")
                print(resultado)
                print("")

            elif resposta == 4:
                tabelas = {'servico', 'valor'}
                print("")
                o_que_atualizar = input("\033[4mQual informação gostaria de atualizar?\033[m ")
                if o_que_atualizar in tabelas:
                    nova_info = input("\033[4mDigite a nova informação: \033[m ")
                    qual_id = input("\033[4mDigite a placa do veiculo para confirmação: \033[m ")
                    Servico.atualizarServico(connObj, o_que_atualizar, nova_info, qual_id)


            elif resposta == 5:
                print("")
                id_exclusao = input("\033[4mInforme o ID para exclusão: \033[m ")
                Servico.deletarServico(connObj, id_exclusao)

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
            continue


#menu_cliente(connObj)
#menu_veiculo(connObj)

# \033[4m Texto \033[m -> sublinhado 
