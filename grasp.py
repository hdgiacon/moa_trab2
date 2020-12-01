import csv
from typing import List
import random

distancias = [      #usar como teste
  [0, 29, 20, 21, 16, 31, 100, 12, 4, 31, 18],    
  [29, 0, 15, 29, 28, 40, 72, 21, 29, 41, 12],    
  [20, 15, 0, 15, 14, 25, 81, 9, 23, 27, 13],  
  [21, 29, 15, 0, 4, 12, 92, 12, 25, 13, 25],     
  [16, 28, 14, 4, 0, 16, 94, 9, 20, 16, 22],      
  [31, 40, 25, 12, 16, 0, 95, 24, 36, 3, 37],     
  [100, 72, 81, 92, 94, 95, 0, 90, 101, 99, 84],   
  [12, 21, 9, 12, 9, 24, 90, 0, 15, 25, 13],      
  [4, 29, 23, 25, 20, 36, 101, 15, 0, 35, 18],
  [31, 41, 27, 13, 16, 3, 99, 25, 35, 0, 38],      
  [18, 12, 13, 25, 22, 37, 84, 13, 18, 38, 0]     
]

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
    #inicializa o ciclo
    cidades = [0, 1, 2]		
                            
    while len(cidades) < len(matriz):
        minimo1 = 999999
        index_min_i1 = -1
        index_min_j1 = -1

        minimo2 = 999999
        index_min_i2 = -1
        index_min_j2 = -1
        
        minimo3 = 999999
        index_min_i3 = -1
        index_min_j3 = -1

        custo = 0
        custo_min = 999999
        index_menor_custo = -1
        custo_total = 0
        
        #seleciona as 3 cidades mais proximas fora do ciclo
        for i in range(len(cidades)):
            for j in range(len(distancias)):
                if j not in cidades and matriz[cidades[i]][j] != 0:
                    if matriz[cidades[i]][j] < minimo1:
                        minimo1 = matriz[cidades[i]][j];
                        index_min_i1 = cidades[i]
                        index_min_j1 = j
                    elif matriz[cidades[i]][j] < minimo2:
                        minimo2 = matriz[cidades[i]][j];
                        index_min_i2 = cidades[i]
                        index_min_j2 = j
                    elif matriz[cidades[i]][j] < minimo3:
                        minimo3 = matriz[cidades[i]][j];
                        index_min_i3 = cidades[i]
                        index_min_j3 = j
                    

        #escolhe uma das 3 cidades aleatoriamente
        aleatorio = random.randint(1,3)
        dados = []  #minimo, index_min_i, index_min_j
        if aleatorio == 1:
            dados.append(minimo1)
            dados.append(index_min_i1)
            dados.append(index_min_j1)
        elif aleatorio == 2:
            dados.append(minimo2)
            dados.append(index_min_i2)
            dados.append(index_min_j2)
        else:
            dados.append(minimo3)
            dados.append(index_min_i3)
            dados.append(index_min_j3)


        #verificação do menor custo para inserir na lista de cidades
        p = 0
        while p < len(cidades):
            if p + 1 == len(cidades):
                cidades.append(dados[2])
            else:
                cidades.insert(p+1,dados[2])
            
            for k in range(len(cidades)):
                if k == len(cidades) - 1:
                    custo = custo + matriz[cidades[k]][0]
                else:
                    custo = custo + matriz[cidades[k]][cidades[k+1]]


            #print("Custo: " + str(custo))
            if custo <= custo_min:
                custo_min = custo
                index_menor_custo = p + 1
            
            cidades.pop(p+1)
            p = p + 1
            custo = 0

        
        #print(str(index_menor_custo))
        #inserção da cidade no local onde o custo total foi minimo
        if index_menor_custo == 0:
            cidades.append(dados[2])
        else:
            cidades.insert(index_menor_custo,dados[2])

        
        print(cidades)


    #calculo do custo total da rota final
    #for k in range(len(cidades)):      #precisa do calculo do custo?
    #	if k == len(cidades) - 1:
    #		custo_total = custo_total + matriz[cidades[k]][0]
    #	else:
    #		custo_total = custo_total + matriz[cidades[k]][cidades[k+1]]
    #
    #cidades.append(0)
    #print(cidades)
    #print("\nCusto total: " + str(custo_total) + "\n")		


def custo():    #como o custo é calculado?
    print()


def reparo():     #o que essa função faz?
    print()


def busca_local():
    print()


#o que é S*, s e s' ?


def main():
    distancias = extrair_dados()   

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



aleat_guloso(distancias)
main()