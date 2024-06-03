from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from controller.produtos import ProdutoController
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
    return ProdutoController().lista_produdos()

@app.post("/v1/finalizar_compra")
async def finalizar_compra(request: Request):
    # criando uma ordem de serviço
    return FinalizarCompraController().criar_ordem_servico(await request.json())
