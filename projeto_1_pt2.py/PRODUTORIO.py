class produtorio_class:
    def __init__(self):
        self._multiplicacao = 1
        self._valor_somados = 0


    def multiplicar_valores(self, valor):
        if valor != 0:
            self._multiplicacao *= valor
            self._valor_somados += 1
    @property
    def media_geometrica(self):
        return self._multiplicacao ** (1 / self._valor_somados)
