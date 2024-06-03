from repository.mysql import MysqlRepository

class PedidosModel:

  def criar_pedido(self, ordem_servico, id_pessoa, produdos):
    # cria a ordem de serviço
    MysqlRepository.dql(f"insert into ordem_servico (numero_ordem, pessoa_id, status_id) values ({ordem_servico}, {id_pessoa}, 1)")
    # recupera o ID da ordem de serviço
    ordem_servico_id = self.ultimo_registro()
    # vincula a ordem de serviço aos produtos
    return self.vincular_produtos_ordem_servico(ordem_servico_id, produdos)
    
  def ultimo_registro(self):
    # recupera o último ID criado na tabela ordem_servico
    ordem_servico_id = MysqlRepository.dql("select id from ordem_servico order by id desc limit 1")

    for i in ordem_servico_id:
        ordem_servico_id = i[0]
    return ordem_servico_id

  # adiciona os registro na tabela entidade de relacionamento (pedidos)
  def vincular_produtos_ordem_servico(self, ordem_servico_id, produtos):
    for item in produtos:
      MysqlRepository.dml(f"insert into pedidos (produto_id, ordem_servico_id) values ({item['id']}, {ordem_servico_id})")
    return True
  
  
