
class estatistica_class():
    def __init__(self):
        self._arquivo_txt = ""
        self._valor = []
        self._peso = []

    def arquivo(self):
        print("a seguir voce ira inserir um arquivo txt que contenha dois valores reais por linha,\nseparados por ';'. O primeiro valor sera o numero enquanto o segundo valor seu peso, com eles, iremos calcular:\n- raiz quadratica media;\n- media aritimetica;\n- media ponderada; \n- media geometrica;\n- media harmonica. ")
        self._arquivo_txt = input("digite o caminho do arquivo txt: ")

    def abrir_arquivo(self):
        self._arquivo_txt = open(self._arquivo_txt, 'r')

    def ler_arquivo(self):
        linha = self._arquivo_txt.readline()
        while linha != "":
            valor, peso = linha.strip().split(';')
            self._valor.append(float(valor))
            self._peso.append(float(peso))
            linha = self._arquivo_txt.readline()

        print(self._valor)
        print(self._peso)
        input("enter")

    def fechar_arquivo(self):
        self._arquivo_txt.close()

    def media_ponderada(self):
        pass

    def media_aritimetica(self):
        pass

    def raiz_quadratica_media(self):
        pass

    def media_geometrica(self):
        pass

    def media_harmonica(self): 
        pass

    def mostrar_resultados(self):
        pass