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
falhas = 0
acertos = 0

"""
    Este trecho de código implementa a política de substituição Least Recently Used (LRU) em um algoritmo de paginação de memória. O conjunto de páginas é representado pelo conjunto 
    "set_aux", enquanto a ordem das páginas é mantida em uma pilha "stack".
    
    Em seguida, o algoritmo percorre cada página "i" no conjunto de páginas "paginador". Se o conjunto "set_aux" ainda não estiver cheio (ou seja, tiver menos elementos que a quantidade 
    de quadros "qtd_frames"), o algoritmo verifica se a página "i" já está presente no conjunto "set_aux". Se sim, a página é movida para o topo da pilha "stack" e contabilizada como um 
    acerto de página. Caso contrário, a página "i" é adicionada ao conjunto "set_aux" e ao topo da pilha "stack", e contabilizada como uma falha de página.
    
    Se o conjunto "set_aux" estiver cheio, o algoritmo verifica se a página "i" já está presente no conjunto. Se sim, a página é movida para o topo da pilha "stack" e contabilizada como 
    um acerto de página. Caso contrário, a página menos recente (ou seja, a que está na base da pilha "stack") é removida tanto do conjunto "set_aux" quanto da pilha "stack", e a página 
    "i" é adicionada ao conjunto e ao topo da pilha, contabilizando uma falha de página.
"""

inicio_paginador = time.time()

for i in paginador:
    if len(set_aux) < qtd_frames:
        if i in set_aux:
            stack.remove(i)
            stack.append(i)
            acertos = acertos + 1
        else:
            set_aux.add(i)
            stack.append(i)
            falhas = falhas + 1
    else:
        if i in set_aux:
            stack.remove(i)
            stack.append(i)
            acertos = acertos + 1
        else:
            recente = stack[0]
            del stack[0]
            set_aux.remove(recente)
            falhas = falhas + 1
            set_aux.add(i)
            stack.append(i)

fim_paginador = time.time()

print("Arquivo lido: " + str(texto))
print("Quantidade de frames: " + str(qtd_frames))
print("Tempo de execução da leitura do arquivo: " + str(round(fim_leitura - inicio_leitura, 2)) + " segundos")
print("Tempo de execução do paginador: " + str(round(fim_paginador - inicio_paginador, 2)) + " segundos")
print("Acertos: " + str(acertos))
print("Falhas: " + str(falhas))