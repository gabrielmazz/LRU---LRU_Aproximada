# Importa os dois arquivos separados que são necessários para o programa
import leitura as L
import funcoes as F
import time

# Chama a função que determina qual arquivo será lido
texto = L.define_leitura()

inicio_leitura = time.time()

# Cria o diretório local para o arquivo que será lido
arquivo = open("traces/" + texto, "r")

dados = []

# Transforma os arquivo de hexadecimal para binário
dados = L.Hex_Bin(dados, arquivo)
        
arquivo.close()

fim_leitura = time.time()

# Apenas da um clear no terminal para ficar mais organizado
F.clear_terminal()

# O usuário determinará a quantidade de frames que serão utilizados
qtd_frames = int(input("Digite a quantidade de frames disponíveis: "))

F.clear_terminal()

# Como não podemos ter frames igual a zero ou abaixo, o programa para a sua execução
if qtd_frames <= 0:
    print("Quantidade de frames não pode ser 0 ou menor!")
    exit()

# Chama a função para criar a lista de paginação 
paginador = F.B2D_pagina(dados)

set_aux = set()
stack = list()
bitRef = list()
acertos = 0
falhas = 0

"""
    Este trecho de código implementa o algoritmo de paginação LRU aproximado. A ideia do algoritmo é manter uma lista de frames (páginas de memória) na memória principal e 
    substituir uma página quando a lista estiver cheia e uma nova página precisar ser carregada. O LRU (Least Recently Used) significa que a página que foi acessada há mais 
    tempo deve ser substituída.
    
    No código, a lista set_aux mantém as páginas que estão atualmente na memória, a lista stack mantém a ordem em que as páginas foram acessadas, e a lista bitRef mantém um 
    bit de referência para cada página, indicando se a página foi referenciada desde a última vez que a lista foi percorrida.
    
    O algoritmo percorre a lista de páginas a serem acessadas paginador e verifica se a página já está na memória. Se sim, atualiza a lista stack para colocar a página mais 
    recentemente acessada no final, atualiza o bit de referência para True e incrementa o contador de acertos. Se a página não está na memória, adiciona à lista set_aux, 
    adiciona à lista stack e à lista bitRef com um novo bit de referência False, e incrementa o contador de falhas.
    
    Quando a lista set_aux estiver cheia e uma nova página precisar ser carregada, o algoritmo percorre a lista bitRef procurando por uma página que não tenha sido referenciada 
    desde a última vez que a lista foi percorrida (ou seja, com o bit de referência False). Se encontrar uma, substitui a página correspondente na lista set_aux e na lista stack 
    com a nova página e atualiza o bit de referência para False. Se não encontrar, substitui a página no início da lista stack (a menos recentemente acessada) e atualiza as listas 
    correspondentes.
"""

inicio_paginador = time.time()

for i in paginador:
    if len(set_aux) < qtd_frames:
        if i in set_aux:            

            indice = stack.index(i)  
            

            if bitRef[indice] == False:     
                bitRef[indice] = True
                
            else:
                stack.remove(i)
                del bitRef[indice]
                stack.append(i)
                bitRef.append(False)
            acertos = acertos + 1
            
        else:
            stack.append(i)
            bitRef.append(False)
            set_aux.add(i)
            falhas = falhas + 1
            
    else:
        
        if i in set_aux:

            indice = stack.index(i)

            if bitRef[indice] == False:
                bitRef[indice] = True
                
            else:
                stack.remove(i)
                del bitRef[indice]
                stack.append(i)
                bitRef.append(False)
            acertos = acertos + 1
        else:
            while bitRef[0] == True:
                recente = stack[0]
                stack.remove(recente)
                del bitRef[0]
                stack.append(recente)
                bitRef.append(False)

            recente = stack[0]
            del stack[0]
            set_aux.remove(recente)
            del bitRef[0]
            falhas = falhas + 1
            set_aux.add(i)
            stack.append(i)
            bitRef.append(False)
    
fim_paginador = time.time()    

print("Arquivo lido: " + str(texto))
print("Quantidade de frames: " + str(qtd_frames))
print("Tempo de execução da leitura do arquivo: " + str(round(fim_leitura - inicio_leitura, 2)) + " segundos")
print("Tempo de execução do paginador: " + str(round(fim_paginador - inicio_paginador, 2)) + " segundos")
print("Acertos: " + str(acertos))
print("Falhas: " + str(falhas))