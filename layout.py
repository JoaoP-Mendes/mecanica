import time 
import sys


def cadastrado(mensagem="Cadastrando", segundos=3):
    for _ in range(segundos):
        for ponto in range(4):
            sys.stdout.write(f"\r{mensagem}{'\033[34m.\033[m' * ponto} ")
            sys.stdout.flush()
            time.sleep(0.25)
    print("\r\033[34mCadastrado com sucesso!\033[m")
    print("")


def carregando(mensagem="Carregando", segundos=3):
    for _ in range(segundos):
        for ponto in range(4):
            sys.stdout.write(f"\r{mensagem}{'\033[34m.\033[m' * ponto}")
            sys.stdout.flush()
            time.sleep(0.25)
    print("")

def excluido(mensagem="Carregando", segundos=3):
    for _ in range(segundos):
        for ponto in range(4):
            sys.stdout.write(f"\r{mensagem}{'\033[34m.\033[m' * ponto}")
            sys.stdout.flush()
            time.sleep(0.25)
    print("\033[31m\nAÇÃO REALIZADA COM SUCESSO! NÃO É POSSÍVEL DESFAZER A AÇÃO\033[m")
    print("")


def atualizado(mensagem="Atualizando", segundos=3):
    for _ in range(segundos):
        for ponto in range(4):
            sys.stdout.write(f"\r{mensagem}{'\033\033[34m.\033[m' * ponto} ")
            sys.stdout.flush()
            time.sleep(0.25)
    print("\r\033[34mAtualizado com sucesso\033[m!")
    print("")

def encerrando(mensagem="Encerrando", segundos=3):
    for _ in range(segundos):
        for ponto in range(4):
            sys.stdout.write(f"\r{mensagem}{'\033\033[34m.\033[m' * ponto}")
            sys.stdout.flush()
            time.sleep(0.25)
        print("")

def voltando(mensagem="Carregando", segundos=2):
    for _ in range(segundos):
        for ponto in range(4):
            sys.stdout.write(f"\r{mensagem}{'\033\033[34m.\033[m' * ponto}")
            sys.stdout.flush()
            time.sleep(0.25)
        print("")