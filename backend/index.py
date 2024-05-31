from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector, json
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="remoto",
  database="turmaformacao"
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/v1/cadastro")
def cadastro_usuario(usuario = Form(), senha = Form()):
    print(usuario, senha)
    return "Cadastro realizado com sucesso!"

@app.get("/v1/produtos")
def produtos():

    # Consulta no banco de dados
    meuCursor = mydb.cursor()
    meuCursor.execute("SELECT * FROM produtos")
    meuResultado = meuCursor.fetchall()
    meuCursor.close()
    mydb.commit()

    # formatação do conteúdo para ser consumido pelo frontend.
    resultado_formatado = []
    for item in meuResultado:
        resultado_formatado.append({
            "id": item[0],
            "nome": item[1],
            "descricao": item[2],
            "preco": item[3],
            "imagem": item[4],
            "quantidade": item[5]
        })

    return resultado_formatado


@app.post("/v1/finalizar_compra")
async def finalizar_compra(request: Request):
    
    itens_carrinho = await request.json()
    
    ordem_servico = str(hash(datetime.datetime.now())).replace("-","")
    id_pessoa = itens_carrinho['id_usuario']
    id_produto = itens_carrinho['itensCarrinho']
    
    
    # criando uma ordem de serviço 
    meuCursor = mydb.cursor()
    meuCursor.execute(f"insert into ordem_servico (numero_ordem, pessoa_id, status_id) values ({ordem_servico}, {id_pessoa}, 1)")

    # recupera o último ID criado na tabela ordem_servico
    meuCursor.execute("select id from ordem_servico order by id desc limit 1")
    ordem_servico_id = meuCursor.fetchall()
    
    for i in ordem_servico_id:
        ordem_servico_id = i[0]

    # adiciona os registro na tabela entidade de relacionamento (pedidos)
    for item in id_produto:
        meuCursor.execute(f"insert into pedidos (produto_id, ordem_servico_id) values ({item['id']}, {ordem_servico_id})")

    meuCursor.close()
    mydb.commit()

    return "Seu pedito foi registrado com sucesso!"

