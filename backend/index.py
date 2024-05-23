from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector, json

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
    meuCursor = mydb.cursor()
    meuCursor.execute("SELECT * FROM produtos")
    meuResultado = meuCursor.fetchall()
    meuCursor.close()

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
def finalizar_compra(itens_carrinho):
    print(itens_carrinho)
    return "Chegou na API de backend!"

