from model.peditos import PedidosModel
import datetime

class FinalizarCompraController:
        
    def criar_ordem_servico(self, data):

        ordem_servico = str(hash(datetime.datetime.now())).replace("-","")
        id_pessoa = data['id_usuario']
        produtos = data['itensCarrinho']

        try:            
            if PedidosModel().criar_pedido(ordem_servico, id_pessoa, produtos):
                return "Seu pedito foi registrado com sucesso!"

        except Exception as error:
             print(error)
             return "Não foi possível registrar seu pedito! Tente novamente mais tarde."
