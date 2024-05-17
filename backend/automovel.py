class Automovel:

    def __init__(self) -> None:
        self.nome_cor   = "red"
        self.__velocidade = 200
        self.aro        = "185/70/13"        
        pass

    def cor(self):
        return "red"

    def  __modelo(self):
        return "Palio"
    
    def  pergar_atributo(self):
        return self.__velocidade

class Caminhoes(Automovel):
    
    def rodas(self):
        return 16    



caminhao = Caminhoes()

print(caminhao.pergar_atributo())


