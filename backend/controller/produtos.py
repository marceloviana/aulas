from model.produtos import ProdutosModel

class ProdutoController:
    
    def lista_produdos(self):
        
        meuResultado = ProdutosModel().lista_produtos()
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
