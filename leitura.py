"""
    Define uma função chamada (define_leitura), que tem a finalidade de permitir ao usuário selecionar um arquivo de texto ou .trace para ser lido posteriormente. 
    A função começa solicitando ao usuário que escolha uma opção de arquivo a partir de uma lista de opções numeradas.
"""
def define_leitura():
    opcoes = int(input("Escolha o arquivo de texto desejado:\n\n" +
                   "Arquivos .txt:\n" +
                   "1 - lu.txt\n" +
                   "2 - mmout.txt\n" +
                   "3 - mmout1.txt\n" + 
                   "4 - sort1.txt\n\n" +
                   "Arquivos .trace:\n" +
                   "5 - bigone.trace\n" +
                   "6 - bzip.trace\n" +
                   "7 - gcc.trace\n" +
                   "8 - sixpack.tarce\n" +
                   "9 - swim.trace\n\n" +
                   "Escolha sua opção: "))

    if opcoes == 1:
        texto = "lu.txt"
    elif opcoes == 2:
        texto = "mmout.txt"
    elif opcoes == 3:
        texto = "mmout1.txt"
    elif opcoes == 4:
        texto = "sort1.txt"
    elif opcoes == 5:
        texto = "bigone.trace"
    elif opcoes == 6:
        texto = "bzip.trace"
    elif opcoes == 7:
        texto = "gcc.trace"
    elif opcoes == 8:
        texto = "sixpack.trace"
    elif opcoes == 9:
        texto = "swim.trace"  

    return texto

"""
    Função que converte uma sequência hexadecimal em uma sequência binária de 4 bits. O código lê cada linha do arquivo e itera sobre cada caractere da linha. Com
    isso temos o retorno com a sequência binária convertida.
"""
def Hex_Bin(dados, arquivo):
    for linha in arquivo:
        auxiliar = []
        for caractere in linha:
            if caractere == ' ':
                auxiliar[len(auxiliar):] = [0,0,0,0]
            elif caractere == '\n':
                break
            elif caractere == '0':
                auxiliar[len(auxiliar):] = [0,0,0,0]
            elif caractere == '1':
                auxiliar[len(auxiliar):] = [0,0,0,1]
            elif caractere == '2':
                auxiliar[len(auxiliar):] = [0,0,1,0]
            elif caractere == '3':
                auxiliar[len(auxiliar):] = [0,0,1,1]
            elif caractere == '4':
                auxiliar[len(auxiliar):] = [0,1,0,0]
            elif caractere == '5':
                auxiliar[len(auxiliar):] = [0,1,0,1]
            elif caractere == '6':
                auxiliar[len(auxiliar):] = [0,1,1,0]
            elif caractere == '7':
                auxiliar[len(auxiliar):] = [0,1,1,1]
            elif caractere == '8':
                auxiliar[len(auxiliar):] = [1,0,0,0]
            elif caractere == '9':
                auxiliar[len(auxiliar):] = [1,0,0,1]
            elif caractere == 'a':
                auxiliar[len(auxiliar):] = [1,0,1,0]
            elif caractere == 'b':
                auxiliar[len(auxiliar):] = [1,0,1,1]
            elif caractere == 'c':
                auxiliar[len(auxiliar):] = [1,1,0,0]
            elif caractere == 'd':
                auxiliar[len(auxiliar):] = [1,1,0,1]
            elif caractere == 'e':
                auxiliar[len(auxiliar):] = [1,1,1,0]
            elif caractere == 'f':
                auxiliar[len(auxiliar):] = [1,1,1,1]
        dados.append(auxiliar)
        
    return dados
