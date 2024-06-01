from repository.produtos import ProdutoRepository

class ProdutoController:
    
    def pegar_produdos(self):
        
        meuResultado = ProdutoRepository().ler("SELECT * FROM produtos")
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
