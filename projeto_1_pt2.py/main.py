import subprocess
from SOMATORIO import Somatorio_class as S
from PRODUTORIO import produtorio_class as P

def seletor():
    subprocess.run('cls', shell=True)
    print("bem vindo!!")
    print("escolha uma das opções abaixo")
    print("======= === === ====== ======")
    print("0 - sair do programa;")
    print("1 - Estatística de uma lista de valores lidos de um arquivo texto")
    print("2 - MMC entre dois valores digitados")
    print("3 - Raiz Cúbica de um valor digitado")
    print("4 - MDC por subtrações sucessivas")
    print("5 - Lista de números de Fibonacci")
    opcao_escolhida = int(input("escolha sua opção:\t"))
    return opcao_escolhida



def func_estatistica():
    subprocess.run('cls', shell=True)
    soma = S()
    prod = P()
    print("a seguir voce ira inserir um arquivo txt que contenha dois valores reais por linha,\nseparados por ';'. O primeiro valor sera o numero enquanto o segundo valor seu peso, com eles, iremos calcular:\n- raiz quadratica media;\n- media aritimetica;\n- media ponderada; \n- media geometrica;\n- media harmonica. ")
    arquivo_txt = input("digite o caminho do arquivo txt: ")
    arquivo_txt = open(arquivo_txt)
    linha = '-'
    while linha != "":
        linha = arquivo_txt.readline()
        if linha != "":
            valor, peso = (linha.strip().split(';'))
            valor = float(valor)
            peso = float(peso)
            soma.somar_valor_com_peso(valor, peso)
            soma.somar_valores(valor)
            soma.somar_inversos(valor)
            prod.multiplicar_valores(valor)
    print(f"media aritimetica: {soma.media_aritimetica}")
    print(f"media ponderada: {soma.media_ponderada}")
    print(f"media harmonica: {soma.media_harmonica}")
    print(f"media geometrica: {prod.media_geometrica}")
    print(f"raiz quadratica media: {soma.raiz_quadratica_media}")
    input("pressione [enter] para continuar!")


def func_mmc():
    pass

def func_raiz():
    pass

def func_mdc():
    pass

def func_fibonacci():
    numero = int(input("Insira a quantidade de numeros da sequencia de fibonnacci:\t"))
    contador = 0
    fibonnacci = 0
    auxiliar2 = 0
    auxiliar1 = 1
    while contador < numero:
        contador += 1
        print(f"{contador}°: {fibonnacci}")
        fibonnacci = auxiliar1 + auxiliar2 
        if contador >= 2:
            auxiliar2 = auxiliar1
            auxiliar1 = fibonnacci
    input("pressione [enter] para continuar")


def principal():
    opcao = -1
    while opcao != 0:
        opcao = seletor()
        if opcao != 0:
            match opcao:
                case 1: func_estatistica()
                case 2: func_mmc()
                case 3: func_raiz()
                case 4: func_mdc()
                case 5: func_fibonacci()
                case _: print("insira uma opção valida\n"); input("pressione [enter] para continuar!")
    subprocess.run('cls', shell=True)  
    print("saindo do programa...")
    print("até breve!")

if __name__ == "__main__":
    principal()