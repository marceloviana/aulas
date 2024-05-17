create database turmaformacao;

CREATE TABLE turmaformacao.pessoa (
	id INT auto_increment NOT NULL,
	nome varchar(100) NOT NULL,
	cpf varchar(11) NOT NULL,
	endereco varchar(255) NOT NULL,
	cartao_credito varchar(100) NULL,
	CONSTRAINT pessoa_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE turmaformacao.produtos (
	id INT auto_increment NOT NULL,
	nome varchar(255) NOT NULL,
	descricao varchar(255) NULL,
	preco FLOAT NOT NULL,
	imagem TEXT NULL,
	quantidade INT NOT NULL,
	CONSTRAINT produtos_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE turmaformacao.pedidos (
	pessoa_id INT NOT NULL,
	produto_id INT NOT NULL,
	CONSTRAINT pedidos_pessoa_FK FOREIGN KEY (pessoa_id) REFERENCES turmaformacao.pessoa(id),
	CONSTRAINT pedidos_produtos_FK FOREIGN KEY (produto_id) REFERENCES turmaformacao.produtos(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;




INSERT INTO produtos (nome, descricao, preco, imagem, quantidade) values ("As 24 Horas da Paixão de Nosso Senhor Jesus Cristo", "Descrição livro - As 24 Horas da Paixão de Nosso Senhor Jesus Cristo", 250, "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/as-24-horas-da-paixao_2020-05-14_09-08-17_0.jpg", 10);
INSERT INTO produtos (nome, descricao, preco, imagem, quantidade) values ("A Cura como Expressão da Misericórdia de Deus", "Descrição livro - A Cura como Expressão da Misericórdia de Deus", 175, "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/a-cura-como-expressao-da-misericordia-de-deus_2022-03-23_15-13-56_0_321.jpg", 10);
INSERT INTO produtos (nome, descricao, preco, imagem, quantidade) values ("5 Passos para Ser Vencedor na Guerra Espiritual Atual", "", 70, "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/livro-5-passos-para-ser-vencedor-na-guerra-atual_2020-05-13_15-11-19_0.jpg", 10);
INSERT INTO produtos (nome, descricao, preco, imagem, quantidade) values ("A Fé de Ratzinger - A Teologia do Papa Bento XVI", "Descrição livro - A Fé de Ratzinger - A Teologia do Papa Bento XVI", 170, "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/a-paixao-de-nosso-senhor-jesus-cristo_2023-06-20_09-13-09_0_367.jpg", 10);


select pessoa.nome, produtos.nome, produtos.preco  from pedidos join pessoa on pessoa.`id` = pedidos.pessoa_id
join produtos on produtos.id = pedidos.produto_id;