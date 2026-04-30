class Somatorio_class():
    def __init__(self):
        self.soma_valores = 0.0
        self.soma_pesos = 0.0
        self.qnt_valores_somados = 0
        self.soma_valor_com_peso = 0.0
        self.soma_inversos = 0.0




    def somar_valores(self, valor):
        self.soma_valores += valor
        self.qnt_valores_somados += 1
       
       


    def somar_valor_com_peso(self, valor, peso):
        self.soma_valor_com_peso += valor * peso
        self.soma_pesos += peso




    def somar_inversos(self, valor):
        if valor != 0:
            self.soma_inversos += 1 / valor
        else:
            raise ZeroDivisionError("Divisao por zero!")
       
    @property
    def media_aritimetica(self):
        return self.soma_valores / self.qnt_valores_somados


    @property
    def media_ponderada(self):
        return self.soma_valor_com_peso / self.soma_pesos
   
    @property
    def media_harmonica(self):
        if self.soma_inversos == 0:
            raise ZeroDivisionError("A soma dos inversos é zero!")
        return self.qnt_valores_somados / self.soma_inversos
   
    @property
    def raiz_quadratica_media(self):
        return (self.soma_valores / self.qnt_valores_somados) ** 0.5
