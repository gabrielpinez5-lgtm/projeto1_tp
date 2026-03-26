from estatistica_lista import estatistica_class as e

import subprocess

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
    parametro = e()
    subprocess.run('cls', shell=True)
    parametro.arquivo()
    parametro.abrir_arquivo()
    parametro.ler_arquivo()
    parametro.fechar_arquivo()
    parametro.media_ponderada()
    parametro.media_aritimetica()
    parametro.raiz_quadratica_media()
    parametro.media_geometrica()
    parametro.media_harmonica()
    parametro.mostrar_resultados()

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