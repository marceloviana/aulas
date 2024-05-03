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
    return [
            {
                "id": 1,
                "nome": "As 24 Horas da Paixão de Nosso Senhor Jesus Cristo",
                "descricao": "Descrição livro - As 24 Horas da Paixão de Nosso Senhor Jesus Cristo",
                "preco": "250",
                "imagem": "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/as-24-horas-da-paixao_2020-05-14_09-08-17_0.jpg"
            },
            {
                "id": 2,
                "nome": "A Cura como Expressão da Misericórdia de Deus",
                "descricao": "Descrição livro - A Cura como Expressão da Misericórdia de Deus",
                "preco": "20",
                "imagem": "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/a-cura-como-expressao-da-misericordia-de-deus_2022-03-23_15-13-56_0_321.jpg"
            },
            {
                "id": 3,
                "nome": "5 Passos para Ser Vencedor na Guerra Espiritual Atual",
                "descricao": "Descrição livro - 5 Passos para Ser Vencedor na Guerra Espiritual Atual",
                "preco": "30",
                "imagem": "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/livro-5-passos-para-ser-vencedor-na-guerra-atual_2020-05-13_15-11-19_0.jpg"
            },
            {
                "id": 4,
                "nome": "A Fé de Ratzinger - A Teologia do Papa Bento XVI",
                "descricao": "Descrição livro - A Fé de Ratzinger - A Teologia do Papa Bento XVI",
                "preco": "20",
                "imagem": "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/a-paixao-de-nosso-senhor-jesus-cristo_2023-06-20_09-13-09_0_367.jpg"
            }
        ]    
