
# Sistema de gerenciamento de Mecanico
Projeto pessoal com Python + MySQL via terminal 

## Objetivo 

Esse projeto tem como objetivo expor minhas tecnicas em desenvolvimento de um sistema simples e funcional, estou aberto a sugestão de melhorias de forma construtiva. 

Esse projeto é um remake do meu trabalho academico da faculdade do repositório: https://github.com/JoaoP-Mendes/autocanica


## Estrutura -- 


mecanica/
├── banco.sql                                     # Script SQL: cria o banco e as 5 tabelas
├── config.py                                     # Dados de conexão com o MySQL
├── banco.py                                      # Classe Bancodados: conexão e execução de queries
├── cliente.py                                    # Classe cliente: CRUD de clientes
├── veiculo.py                                    # Classe veiculo: CRUD de veiculos
├── servico.py                                    # classe servico: CRUD de serviço
├── ordem_servico.py                              # classe ordem_Servico: CRUD de ordem de serviço e itens serviço
├── layout.py                                     # Funções interativas com terminal - timers
├── menu.py                                       # Fluxo de menus classes
└── main.py                                       # Menu para inicio do terminal, ponto de entrada do programa



## Como rodar

### 1. Instalar a biblioteca 
pip install pymysql
### 2. Criar o banco de dados 
Execute o conteúdo do banco.sql no MySQL. Isso cria o banco mecanica e as 5 tabelas: cliente, veiculo, servico, ordem_servico e itens_servico.

### 3. Configurar a conexão
Edite config.py com o usuário/senha do seu MySQL local:

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "passwd": "sua_senha_aqui",
    "database": "mecanica"
}

### 4. Rodar o programa
python main.py

Isso abre o menu principal, com acesso aos 4 submenus: cliente, veiculo, serviço, começar trabalho.


## Arquitetura 
O projeto é dividido em camadas:

config.py — guarda os dados de conexão (host, user, senha, database).
banco.py (classe Bancodados) — responsável por conectar, desconectar e executar qualquer query, usando parâmetros preparados (%s + tupla de valores) para evitar SQL Injection. Tem os métodos conectar(), desconectar() e executar(query, valor=()), que cria o cursor, roda a query e devolve o resultado (fetchall() para SELECT, lastrowid após commit para INSERT/UPDATE/DELETE).
cliente.py, veiculo.py, servico.py, ordem_servico.py — cada classe concentra o SQL e as regras da sua entidade. Métodos de cadastro (que representam um registro específico sendo criado) são métodos de instância; métodos de consulta/manutenção geral (listar, buscar, atualizar, remover) são @staticmethod, recebendo a conexão como parâmetro.
layout.py — funções auxiliares de apresentação no terminal (mensagens de carregamento, cores), sem lógica de negócio.
menu.py — uma função de menu por entidade (menu_cliente(), menu_veiculo(), etc), cada uma com seu próprio laço e opções.
main.py — cria a conexão uma única vez e tem o menu principal que direciona para o submenu escolhido.

## Classes 

### Cliente
Usa cpf como chave primária. O CPF é validado por @property/@setter no momento da atribuição (recusa valores com tamanho diferente de 11 caracteres). Métodos: novoCliente() (instância), listarClientes(), buscarPorCpf(), deletarCliente(), atualizarCliente() (estáticos). deletarCliente() trata especificamente IntegrityError, avisando quando o cliente possui veículos vinculados antes de permitir a exclusão.

### Veiculo
Usa id (AUTO_INCREMENT) como PK, com placa marcada como UNIQUE, e cpf_cliente como chave estrangeira para cliente. Métodos: novoVeiculo() (instância), listarVeiculos(), buscarPorPlaca(), deletarVeiculo(), atualizarVeiculo() (estáticos).

### Servico
Catálogo de serviços oferecidos pela oficina (nome e valor fixo). Métodos: novoServico() (instância), listarServicos(), atualizarServico(), deletarServico() (estáticos).

### Ordem_Servico
Representa a visita de um veículo à oficina. Ao ser criada, calcula a data_inicio automaticamente (date.today()). Também concentra os métodos de itens_servico — a tabela associativa que resolve a relação muitos-para-muitos entre ordens e serviços. Métodos: novaOrdemServico() (instância), listarOrdens(), buscarPorId(), deletarOrdem(), atualizarStatus(), adicionarItem(), listarItensDaOrdem(), removerItem() (estáticos).

## Tabelas (banco.sql)
> cliente: cpf (PK), nome, data_nascimento, telefone, ativo_sn
> veiculo: id (PK), cpf_cliente (FK), placa (UNIQUE), ano, km_atual, marca
> servico: id (PK), servico, valor
> ordem_servico: id (PK), id_veiculo (FK), data_inicio, status
> itens_servico: id (PK), id_ordem_servico (FK), id_servico (FK) — tabela associativa entre ordem_servico e servico

## Modelagem
O diagrama entidade-relacionamento foi desenhado antes da implementação, com as seguintes decisões:

Cliente ↔ Veiculo: relação 1:N (um cliente pode ter vários veículos)
Veiculo ↔ Ordem_servico: relação 1:N (um veículo pode ter várias ordens)
Ordem_servico ↔ Servico: relação N:N, resolvida pela tabela associativa itens_servico

https://app.brmodeloweb.com/publicview/6a83b96ab01df802fa95402d - Modelo conceitual 
https://app.brmodeloweb.com/publicview/6a83b0ebb01df802fa953ee9 - Modelo logico