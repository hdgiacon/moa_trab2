import csv
from typing import List

def extrair_dados():
    with open('USCA312.csv', 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv, delimiter = ',')

        k = 0
        cidades: List[str] = []
        for coluna in leitor:
            cidades.insert(k,str(coluna))
            k += 1

        aux = []
        aux2 = []
        dist: List[List[int]] = []

        flag = False
        i1 = 0
        for i in cidades:
            aux = i.replace('\'',' ').replace(',',' ').replace(']',' ').split()
            if flag == True:
                j1 = 0
                for j in range(len(aux)):
                    if aux[j].isdigit():
                        aux2.append(int(aux[j]))
                dist.append(aux2)
                aux2 = []
            flag = True
    
    return dist


def aleat_guloso(matriz):
    print()

def custo():    #como o custo é calculado?
    print()

def reparo():     #o que essa função faz?
    print()

def busca_local():
    print()

#o que é S*, s e s' ?

def main():
    #distancias = extrair_dados()   

    #custo(S*) = inf
    
    #while qual o criterio de parada? :
        #s = aleat_guloso()     #inserção mais proxima modificada
        #if s não for viavel? : o que é ser viavel?
            #s = reparo(s)

        #s' = busca_local()    #o que é s'?
        #if custo(s') < custo (S*):
            #S* = s'
    
    #return S*
    print()




main()