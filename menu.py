from cliente import Cliente
from veiculo import Veiculo
from servico import Servico
from ordem_servico import ordem_Servico
from layout import voltando

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
                voltando()
                break

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
                voltando()
                break


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
                voltando()
                break


            else:
                print("")
                print("\033[31mERRO\033[m: Ação não reconhecida, informe uma ação valida")
                print("")
                continue

        except Exception as e:
            print(f"An error occured: {e}")
            continue

def menu_ordem(connObj):
    while True:
        try:
            resposta = int(input("\033[36m----- MENU ORDEM SERVIÇO -----\033[m\n1 - Nova ordem de serviço \n2 - Listar \n3 - Buscar por ID \n4 - Atualizar status \n5 - Deletar ordem \n6 - Começar trabalho \n7 - Listar trabalhos \n8 - Cancelar \n0 - Voltar para o menu\nResposta: "))
            if resposta == 1:
                print("")
                idveiculo = input("\033[4mDigite o ID do veiculo\033[m: ") 

                ordem = ordem_Servico(connObj, idveiculo)
                ordem.novaOrdemServico()

            elif resposta == 2: 
                print("")
                lista_ordem = ordem_Servico.listarOrdens(connObj)
                print("ORDENS CRIADAS: ")
                for cada_ordem in lista_ordem:
                    print(cada_ordem)
                print("")

            elif resposta == 3:
                print("")
                id_busca_ordem = input(" \033[4mInforme o ID para busca:\033[m ")
                resultado = ordem_Servico.buscarPorId(connObj, id_busca_ordem)
                print("RESULTADO BUSCA: ")
                print(resultado)
                print("")

            elif resposta == 4:
                tabelas = {'status'}
                print("")
                o_que_atualizar = input("\033[4mQual status atual da ordem?\033[m \n > Iniciado \n > Em processo \n > Finalizado \nResposta: ")
                if o_que_atualizar in tabelas:
                    nova_info = input("\033[4mDigite a nova informação: \033[m ")
                    qual_id = input("\033[4mDigite da ordem para confirmação: \033[m ")
                    ordem_Servico.atualizarStatus(connObj, o_que_atualizar, nova_info, qual_id)


            elif resposta == 5:
                print("")
                id_exclusao_ordem = input("\033[4mInforme o ID para exclusão: \033[m ")
                ordem_Servico.deletarOrdem(connObj, id_exclusao_ordem)


            elif resposta == 6:
                print("")
                id_ordem_servico = input("\033[4mInforme o ID da ordem de serviço para começar o trabalho:\033[m ")
                id_servico = input("\033[4mInforme o ID do serviço para começar o trabalho:\033[m ")
                ordem_Servico.adicionarItem(connObj, id_ordem_servico, id_servico)

            elif resposta == 7:
                print("")
                lista_trabalhos = ordem_Servico.listarItens(connObj)
                print("TRABALHOS: ")
                for cada_trabalho in lista_trabalhos:
                    print(cada_trabalho)
                print("")

            elif resposta == 8:
                print("")
                id_trabalho = input("\033[4mInforme o id do trabalho para exclusão:\033[m ")
                ordem_Servico.deletarItem(connObj, id_trabalho)
                print("")

            elif resposta == 0:
                print("")
                voltando()
                break

            else:
                print("")
                print("\033[31mERRO\033[m: Ação não reconhecida, informe uma ação valida")
                print("")
                continue

        except Exception as e:
            print(f"Algo inesperado aconteceu: {e}")
            continue

#menu_cliente(connObj)
#menu_veiculo(connObj)
#menu_ordem(connObj)

# \033[4m Texto \033[m -> sublinhado 
