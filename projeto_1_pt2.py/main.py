import subprocess
from SOMATORIO import Somatorio_class as S

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
    soma = S()
    print("a seguir voce ira inserir um arquivo txt que contenha dois valores reais por linha,\nseparados por ';'. O primeiro valor sera o numero enquanto o segundo valor seu peso, com eles, iremos calcular:\n- raiz quadratica media;\n- media aritimetica;\n- media ponderada; \n- media geometrica;\n- media harmonica. ")
    arquivo_txt = input("digite o caminho do arquivo txt: ")
    arquivo_txt = open(arquivo_txt)
    linha = '-'
    while linha != "":
        linha = arquivo_txt.readline()
        if linha != "":
            valor, peso = linha.strip().split(';')
            soma.somar_valor_com_peso(valor, peso)
    print(soma.media_ponderada)


def func_mmc():
    pass

def func_raiz():
    pass

def func_mdc():
    pass

def func_fibonacci():
    pass


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