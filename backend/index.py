from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
import datetime
from controller.produto import ProdutoController
from controller.finalizar_compra import FinalizarCompraController

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
    return "Cadastro realizado com sucesso!"

@app.get("/v1/produtos")
def produtos():
    # Consulta no banco de dados
    return ProdutoController().pegar_produdos()

@app.post("/v1/finalizar_compra")
async def finalizar_compra(request: Request):    
    itens_carrinho = await request.json()
    ordem_servico = str(hash(datetime.datetime.now())).replace("-","")
    id_pessoa = itens_carrinho['id_usuario']
    produtos = itens_carrinho['itensCarrinho']
    
    # criando uma ordem de serviço
    if FinalizarCompraController().criar_ordem_servico(ordem_servico, id_pessoa, produtos):
        return "Seu pedito foi registrado com sucesso!"
    return "Não foi possível registrar seu pedito! Tente novamente mais tarde."
