from repository.produtos import ProdutoRepository

class FinalizarCompraController:
    
    def pegar_produdos(self):
            return ProdutoRepository()
        
    def criar_ordem_servico(self, ordem_servico, id_pessoa, produtos):
        try:
            sql = f"insert into ordem_servico (numero_ordem, pessoa_id, status_id) values ({ordem_servico}, {id_pessoa}, 1)"
            ProdutoRepository().criar(sql)

            # recupera o último ID criado na tabela ordem_servico
            ordem_servico_id = self.ler_ultimo_registro()

            for i in ordem_servico_id:
                ordem_servico_id = i[0]

            # adiciona os registro na tabela entidade de relacionamento (pedidos)
            for item in produtos:
                FinalizarCompraController().criar_pedido(item['id'], ordem_servico_id)
            return True
        except Exception as error:
             print(error)
             return False
        
    
    def ler_ultimo_registro(self):
         sql = "select id from ordem_servico order by id desc limit 1"
         return ProdutoRepository().ler(sql)

    def criar_pedido(self, item_produto, ordem_servico_id):
        sql = f"insert into pedidos (produto_id, ordem_servico_id) values ({item_produto}, {ordem_servico_id})"
        return ProdutoRepository().criar(sql)
