class Somatorio_class():
    def __init__(self):
        self.soma_valores = 0.0
        self.soma_pesos = 0.0
        self.qnt_valores_somados = 0
        self.soma_valor_com_peso = 0.0

    def numero_valores(self, num):
        self.qnt_valores_somados = num

    def aritimetica(self):
        return self.soma_valores / self.qnt_valores_somados
    
    def ponderada(self):
        self.soma_valor_com_peso

    def somar(self, valor):
        pass

    def somar_valor_com_peso(self, valor, peso):
        self.soma_valor_com_peso += valor * peso
        self.soma_pesos += peso
        self.qnt_valores_somados += 1

    @property
    def media_ponderada(self):
        return self.soma_valor_com_peso / self.soma_pesos
        