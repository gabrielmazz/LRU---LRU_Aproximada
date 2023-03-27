import os

def clear_terminal():
    if os.name == 'nt': # para sistemas Windows
        os.system('cls')
    else: # para sistemas Unix
        os.system('clear')

"""
    A função recebe uma lista chamada "dados" como entrada. Essa lista contém valores binários, que representam páginas de memória. A função converte esses valores 
    binários para valores decimais (base 10) e armazena em uma nova lista chamada "paginador". Para cada elemento da lista de entrada, a função itera pelos seus elementos 
    (de 0 a 19) e calcula o valor decimal equivalente, utilizando a fórmula: 2 elevado à potência do índice (19-j) multiplicado pelo valor binário correspondente a esse índice. 
    O resultado da operação é armazenado na variável "somatorio". O valor dessa variável é então adicionado à lista "paginador". No final, a função retorna a lista "paginador" 
    com os valores convertidos para decimal.
"""
def B2D_pagina(dados):
    paginador = list()
    for i in range(len(dados)):
        somatorio = 0
        for j in range(0, 20):
            somatorio = somatorio + (dados[i][j] * (2 ** (19-j)))
        paginador.append(somatorio)
    return paginador