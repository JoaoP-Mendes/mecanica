from banco import BancoDados
from layout import encerrando
from menu import menu_cliente, menu_veiculo, menu_servico, menu_ordem

connObj = BancoDados()
connObj.conectar()


while True:
    escolha = int(input("------------ INICIANDO SISTEMA ------------\nEscolha uma opção para começar\n > 1 - Clientes\n > 2 - Veiculo\n > 3 - Serviços\n > 4 - Começar trabalho \n > 0 - Sair \nResposta: "))
    if escolha == 1:
        menu_cliente(connObj)

    elif escolha == 2:
        menu_veiculo(connObj)

    elif escolha == 3: 
        menu_servico(connObj)

    elif escolha == 4:
        menu_ordem(connObj)

    elif escolha == 0:
        encerrando()
