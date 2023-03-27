# Implementação da LRU e LRU Aproximada

### Trabalho de Sistemas Operacionais
>Colaboradores: *Gabriel Mazzuco* ([Github Profile](https://github.com/gabrielmazz)), *Rodrigo Rocha* ([Github Profile](https://github.com/Rodrigo2603)) e *Gabriel Norato* ([Github Profile](https://github.com/iMaGiNaTrOn))
- 3ª ano de Ciências da Computação
---
### Introdução

O código de implementação dos algoritmos de paginação LRU e LRU Aproximada, foram desenvolvidos em Python. Os algoritmos utilizam como base a leitura de arquivos que contém informações de páginas em formato hexadecimal, e as transforma em formato binário. O código foi dividido em três arquivos distintos, sendo um para as funções principais `(funcoes.py)`, outro para a leitura dos arquivos `(leitura.py)` e o arquivo de execução do algoritmo `(lru.py / lru_aproximada.py)`.

```python
import leitura as L
import funcoes as F
```

### Funcionamento

#### LRU Pura

O algoritmo LRU (Least Recently Used), ou Menos Recentemente Utilizado, é uma política de substituição de páginas de memória, que visa manter em memória as páginas que foram acessadas recentemente. Quando o espaço de memória se esgota, o algoritmo remove da memória a página que foi acessada há mais tempo.

O código do algoritmo LRU Pura está contido no arquivo algoritmos.py. Após a leitura do arquivo de entrada, o usuário deve informar a quantidade de frames disponíveis. Em seguida, o algoritmo percorre cada página do arquivo de entrada e realiza a verificação se a página já se encontra presente na memória. Caso a página já esteja presente, ela é movida para o topo da pilha e é contabilizada como acerto. Caso contrário, a página é adicionada ao topo da pilha e contabilizada como falha.

Caso o número de frames esteja esgotado, o algoritmo irá remover da pilha a página que foi acessada há mais tempo. Em seguida, a página atual será adicionada no topo da pilha.

##### Código exemplo da LRU Pura

```python
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
```

#### LRU Aproximada

O algoritmo LRU Aproximada é uma implementação que utiliza o conceito de bits de referência. Cada página é representada por um bit de referência que é definido como 1 quando a página é acessada e como 0 caso contrário. Durante a execução do algoritmo, os bits de referência são atualizados e, em caso de conflito, é removida a página com o bit de referência mais antigo.

O código do algoritmo LRU Aproximada está contido no arquivo algoritmos.py. Assim como no algoritmo LRU Pura, após a leitura do arquivo de entrada, o usuário deve informar a quantidade de frames disponíveis. Em seguida, o algoritmo percorre cada página do arquivo de entrada e realiza a verificação se a página já se encontra presente na memória. Caso a página já esteja presente, o bit de referência da página é atualizado para 1 e é contabilizada como acerto. Caso contrário, é realizada a verificação dos bits de referência de todas as páginas presentes na memória. A página com o bit de referência mais antigo é removida e a nova página é adicionada em seu lugar.

Caso o número de frames esteja esgotado, o algoritmo irá remover da memória a página com o bit de referência mais antigo. Em seguida, a página atual será adicionada ao espaço liberado.

##### Código exemplo da LRU Aproximada

```python
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
```

### Arquivos .txt ou .trace

Dentro da aplicação LRU (Least Recently Used), é possível utilizar arquivos de entrada com extensão .txt ou .trace, contendo entradas hexadecimais que variam de 100 leituras a 400000. Esses arquivos são importantes para simular o comportamento da memória cache em diferentes situações.

Ao executar a aplicação LRU com um arquivo de entrada, o programa irá ler as entradas do arquivo e armazená-las em uma estrutura de dados, simulando a memória cache. Em seguida, a aplicação LRU irá processar as entradas de acordo com o algoritmo LRU, determinando quais entradas devem ser mantidas na memória cache e quais devem ser removidas.

Os arquivos de entrada com maiores quantidades de leituras ou entradas hexadecimais podem ser usados para testar o desempenho da aplicação LRU em situações de alta demanda de acesso à memória cache. Já os arquivos de entrada com menor quantidade de leituras podem ser usados para testar a eficácia do algoritmo LRU em situações com pouca demanda de acesso à memória cache.

### Conversor de Hexadecimal para Binário

Esta função recebe como entrada um arquivo contendo sequências em formato hexadecimal e converte cada caractere para sua correspondente sequência binária de 4 bits. O resultado é armazenado em uma lista de listas de 4 bits.

O processo é realizado lendo cada linha do arquivo e iterando sobre cada caractere da linha. Caso o caractere seja um espaço ou uma quebra de linha, a sequência binária correspondente é adicionada à lista auxiliar. Caso contrário, o caractere é convertido para sua sequência binária correspondente e adicionado à lista auxiliar.

O resultado final é uma lista de listas de 4 bits contendo a sequência binária correspondente a cada caractere do arquivo de entrada.

```python
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
            # Códigos para os outros numeros e letras
            elif caractere == 'e':
                auxiliar[len(auxiliar):] = [1,1,1,0]
            elif caractere == 'f':
                auxiliar[len(auxiliar):] = [1,1,1,1]
        dados.append(auxiliar)
    return dados
```

### Conversor de Binário para Decimal

Este código apresenta a função B2D_pagina, que recebe uma lista de dados em binário e retorna uma lista com a conversão de cada elemento para decimal, usando um paginador.

O paginador é uma técnica utilizada para a conversão de números binários em decimais, em que cada bit do número binário é multiplicado por 2 elevado à potência do índice do bit (considerando a ordem dos bits da direita para a esquerda) e somado ao somatório geral. Essa técnica é aplicada neste código utilizando dois loops for, em que o loop mais externo itera sobre cada elemento da lista de dados e o loop interno itera sobre cada bit do número binário, calculando o valor decimal do número.

```python
def B2D_pagina(dados):
    paginador = list()
    for i in range(len(dados)):
        somatorio = 0
        for j in range(0, 20):
            somatorio = somatorio + (dados[i][j] * (2 ** (19-j)))
        paginador.append(somatorio)
    return paginador
```

Ao final do processamento, a função retorna uma lista com os valores decimais correspondentes a cada número binário da lista de entrada.

### Saida para o usuário

O algoritmo irá fornecer as seguintes informações ao usuário, todas essas informações serão exibidas para o usuário após a execução do algoritmo, permitindo que ele avalie o desempenho do programa e verifique os resultados obtidos.

-   O arquivo que foi lido pelo programa será exibido na tela;
-   A quantidade de frames presentes no arquivo será apresentada;
-   O tempo de execução da leitura do arquivo em segundos será mostrado;
-   O tempo de execução do paginador também será apresentado em segundos;
-   O número de acertos identificados pelo algoritmo será exibido;
-   O número de falhas encontradas pelo algoritmo também será apresentado.

### Como executar

Para executar o código de LRU puro ou LRU aproximada, siga os seguintes passos:

1.  Clone o repositório com o código em sua máquina local.
```bash
git clone https://github.com/gabrielmazz/LRU---LRU_Aproximada.git
```

2.  Instale o Python 3 em sua máquina, caso ainda não tenha feito.
```bash
sudo apt-get install python3
```

3.  Abra um terminal na pasta do projeto.
   
4.  Digite `python` `LRU.py` ou `python LRU_aproximado.py`, dependendo do algoritmo que deseja executar.
```python
python3 LRU.py
python3 LRU_aproximado.py
```

5.  Siga as instruções exibidas no terminal para escolher o arquivo de entrada e a quantidade de frames disponíveis.
   
6.  Aguarde até que o programa execute completamente.
   
7.  Serão exibidos no terminal o tempo de execução, o número de acertos e o número de falhas.

É importante lembrar que os arquivos de entrada devem estar na pasta "traces" e possuir a extensão ".txt". Além disso, é necessário ter os arquivos "leitura.py" e "funcoes.py" na mesma pasta que o arquivo do algoritmo escolhido.
