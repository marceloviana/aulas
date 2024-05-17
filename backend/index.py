from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

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

    # 1. conecta ao banco de dados turmaformacao. Como conectar o Python no banco de dados Mysql?
    # 2. lista todos os produtos
    # 3. entrega todos os produtos para o frontend
    # 4. registra meus pedidos
    # 5. lista os pedidos, relacionando-os entre pessoa e produto.

    return []
