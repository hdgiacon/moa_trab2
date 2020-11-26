import csv
from typing import List

with open('USCA312.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter = ',')

    k = 0
    cidades: List[str] = []
    for coluna in leitor:
        cidades.insert(k,str(coluna))
        k += 1

    aux = []
    aux2 = []
    distancias: List[List[int]] = []

    flag = False
    i1 = 0
    for i in cidades:
        aux = i.replace('\'',' ').replace(',',' ').replace(']',' ').split()
        if flag == True:
            j1 = 0
            for j in range(len(aux)):
                if aux[j].isdigit():
                    aux2.append(int(aux[j]))
            distancias.append(aux2)
            aux2 = []
        flag = True



#a entrada é uma matriz quadrada?
#for i in range(len(distancias)):
#    print(str(distancias[i]))
    

    
