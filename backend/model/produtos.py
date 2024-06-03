from repository.mysql import MysqlRepository

class ProdutosModel:

    def lista_produtos(self):
        return MysqlRepository.dql("SELECT * FROM produtos")

    
