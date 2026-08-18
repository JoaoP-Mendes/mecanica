CREATE DATABASE mecanica;
USE mecanica;

CREATE TABLE cliente (
	cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    ativo_sn ENUM('S', 'N') DEFAULT 'S'
) DEFAULT CHARSET = utf8mb4;

CREATE TABLE veiculo (
	id INT PRIMARY KEY AUTO_INCREMENT,
    cpf_cliente VARCHAR(11) NOT NULL, 
    placa VARCHAR(7) NOT NULL UNIQUE,
    ano YEAR NOT NULL,
    km_atual INT NOT NULL DEFAULT 0,
    marca VARCHAR(30) NOT NULL, 
    CONSTRAINT cliente_cpf FOREIGN KEY (cpf_cliente) REFERENCES cliente(cpf)
) DEFAULT CHARSET = utf8mb4;

CREATE TABLE servico (
	id INT PRIMARY KEY AUTO_INCREMENT,
    servico VARCHAR(80) NOT NULL,
    valor DECIMAL(5, 2) NOT NULL
)  DEFAULT CHARSET = utf8mb4;


CREATE TABLE ordem_servico (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_veiculo INT NOT NULL,
    data_inicio DATE NOT NULL,
   	status ENUM('Iniciado','Em processo','Finalizado') DEFAULT 'Iniciado',
    CONSTRAINT veiculo_id FOREIGN KEY (id_veiculo) REFERENCES veiculo(id)
) DEFAULT CHARSET = utf8mb4;

CREATE TABLE itens_servico (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_ordem_servico INT NOT NULL,
    id_servico INT NOT NULL,
    valor_atual DECIMAL(5, 2) NOT NULL,-- Aqui o valor será guardado em uma váriavel para depois inserir no SQL
    CONSTRAINT ordem_servico_id FOREIGN KEY (id_ordem_servico) REFERENCES ordem_servico(id),
    CONSTRAINT servico_id FOREIGN KEY (id_servico) REFERENCES servico(id)
)  DEFAULT CHARSET = utf8mb4;