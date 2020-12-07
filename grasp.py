from typing import List
import csv
import random

distancias_ex = [      #usar como teste
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

def extrair_dados():    #extrai os dados do arquivo .csv
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
            for j in range(len(matriz)):
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
	
    return cidades


def custo(rota,matriz):
    custo = 0
    for k in range(len(rota)):
        if k == len(rota) - 1:
            custo = custo + matriz[rota[k]][0]
        else:
            custo = custo + matriz[rota[k]][rota[k+1]]

    return custo


def vizinhanca(solucao_aleatoria):      #estrategia N1
    vizinhanca = []
    aux_vizinhanca = []
    aux1 = 0
    aux2 = 0
    for i in range(len(solucao_aleatoria) - 1):
        aux_vizinhanca =  solucao_aleatoria.copy()
        aux1 = solucao_aleatoria[i]
        aux2 = solucao_aleatoria[i+1]

        aux_vizinhanca[i] = aux2
        aux_vizinhanca[i+1] = aux1
        
        vizinhanca.append(aux_vizinhanca)
    
    return vizinhanca


def busca_local(solucao_aleatoria, matriz):
    menor_custo = 99999999999
    menor_index = 0
    aux_custo = 0
    vizinhos = vizinhanca(solucao_aleatoria)

    for i in range(len(vizinhos)):
            aux_custo = custo(vizinhos[i],matriz)
            if aux_custo < menor_custo:
                menor_custo = aux_custo
                menor_index = i

    return vizinhos[menor_index]    #retornar a rota de menor custo


#S*=solucao otima, S=solucao aleatoria, S'= solucao resultante da busca local
# os S's representam a rota
#custo = distancia

#verifica todos os custos dos vizinhos da rota atual
#escolhe a rota de menor custo
#faz o mesmo processo pra nova rota
#se nao houver uma rota de menor custo do que atual, retorne essa rota


def grasp():
    #distancias = extrair_dados()   # .csv
    distancias = distancias_ex
    custo_final = 0   
    flag = True        #custo(S*) = inf
    
    k = 0
    iteracoes = int(input("\nDigite o numero de iterações do GRASP: "))

    while k < iteracoes:
        S = aleat_guloso(distancias)     #inserção mais proxima modificada

        S_linha = busca_local(S,distancias)

        if flag == True:        #para S_estrela ter um primeiro valor para haver comparação 
            S_estrela = S_linha
            flag = False    
        elif custo(S_linha,distancias) < custo(S_estrela,distancias):
            S_estrela = S_linha
    
        k += 1

    #calculo do custo final
    custo_final = custo(S_estrela,distancias)

    return S_estrela, custo_final



caminho = []
custo_f = 0

caminho,custo_f = grasp()
print(caminho)
print("Custo: " + str(custo_f))