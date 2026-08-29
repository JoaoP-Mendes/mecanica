import time 
import sys

def cadastrado(mensagem="Cadastrando", segundos=3):
    for _ in range(segundos):
        for ponto in range(4):
            sys.stdout.write(f"\r{mensagem}{'\033[32m.\033[m' * ponto} ")
            sys.stdout.flush()
            time.sleep(0.25)
    print("\r\033[34mCadastrado com sucesso\033[m!")

cadastrado()