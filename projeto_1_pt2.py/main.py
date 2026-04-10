import subprocess
from somatorio import Somatorio_class as S
from produtorio import produtorio_class as P

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


def func_mmc(v1, v2):
    numero_que_divide   = 2
    divisor = 1
    while numero_que_divide <= v1 or numero_que_divide <= v2:
        if v1 % numero_que_divide == 0 and v2 % numero_que_divide == 0:
            v1 /= numero_que_divide
            v2 /= numero_que_divide
            divisor *= numero_que_divide
        else:
            if v1 % numero_que_divide == 0:
                v1 /= numero_que_divide
                divisor *= numero_que_divide
            elif v2 % numero_que_divide == 0:
                v2 /= numero_que_divide
                divisor *= numero_que_divide
            else: numero_que_divide += 1
    print(f"o mmc é {divisor}")

    


def func_raiz_cubica(valor, erro):
    palpite = 1
    novo_valor = 0
    while palpite - novo_valor > erro:
        print(f"{palpite}\t{(valor/palpite**2 + 2*palpite)/3} ")
        novo = (valor/palpite**2 + 2*palpite)/3
    print(f"o valor é {palpite}")


def func_mdc(v1,v2):
    numero_que_divide   = 2
    divisor = 1
    while numero_que_divide <= v1 or numero_que_divide <= v2:
        if v1 % numero_que_divide == 0 and v2 % numero_que_divide == 0:
            v1 /= numero_que_divide
            v2 /= numero_que_divide
            divisor *= numero_que_divide
        else:
            if v1 % numero_que_divide == 0:
                v1 /= numero_que_divide
            elif v2 % numero_que_divide == 0:
                v2 /= numero_que_divide
            else: numero_que_divide += 1
    print(f"o mdc é {divisor}")

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
                case 2: 
                    repetir = 'y'
                    while repetir != 'n':
                        v1 = int(input("insira o primeiro valor:\t"))
                        v2 = int(input("insira o segundo valor:\t"))
                        func_mmc(v1, v2)
                        repetir = input("deseja calcular o mmc de outros numeros? [y/n]:\t").lower()
                case 3:
                    repetir = 'y'
                    while repetir != 'n':
                        v1 = int(input("digite o numero que deseje calcular a raiz cubica:\t"))
                        v2 = float(input("digite a margem maxima de erro:\t"))
                        func_raiz_cubica(v1,v2)
                        repetir = input("deseja calcular o mmc de outros numeros? [y/n]:\t").lower()
                case 4:
                    
                    while repetir != 'n':
                        v1 = int(input("insira o primeiro valor:\t"))
                        v2 = int(input("insira o segundo valor:\t"))
                        func_mdc(v1, v2)
                        repetir = input("deseja calcular o mmc de outros numeros? [y/n]:\t").lower()
                case 5: func_fibonacci()
                case _: print("insira uma opção valida\n"); input("pressione [enter] para continuar!")
    subprocess.run('cls', shell=True)  
    print("saindo do programa...")
    print("até breve!")

if __name__ == "__main__":
    principal()
