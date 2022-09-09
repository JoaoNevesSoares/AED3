import numpy as np
from sys import maxsize
from itertools import combinations
import random

#sub-rotine to merge two lists without duplicate elements
def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)
    return a

#sub-rotine to remove duplicates from a list without messing with order
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def prim(G):
    selected_node = np.zeros(G[0,:].size)
    no_edge = 0
    selected_node[0] = True
    #mst = [0 for _ in range(G[0,:].size)] #iniciliza a lista mst com tamanho 11 xd
    mst = []
    while (no_edge < (G[0,:].size -1)):
    
        minimum = maxsize
        a = 0
        b = 0
        for m in range(G[0,:].size):
            if selected_node[m]:
                for n in range(G[0,:].size):
                    if ((not selected_node[n]) and G[m][n]):  
                        # not in selected and there is an edge
                        if minimum > G[m][n]:
                            minimum = G[m][n]
                            a = m
                            b = n
        mst.append((a,b,G[a][b]))
        #print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
        selected_node[b] = True
        no_edge += 1
    return mst

def fides(G,edges):

    ## Calculate the set of vertices O with odd degree in T
    degree= np.zeros(G[0,:].size)
    O =[]
    for edge in edges:
        degree[edge[0]] +=1
        degree[edge[1]] +=1
    for i in range(0,degree.size):
        if degree[i]%2 !=0:
            O.append(i)
    #Form the subgraph of M using only the vertices of O
    #Construct a minimum-weight perfect Patching BP in this subgraph
    M = []
    for matches in combinations(O,2):
        M.append((matches[0],matches[1],G[matches[0]][matches[1]]))
    min_cost = maxsize
    while M:
        A = random.choice(M)
        M.remove(A)
        for match in M:
            if ((match[0] != A[0] and match[0] != A[1]) and (match[1] != A[0] and match[1] !=A[1])):
                path_cost = A[2] + match[2]
                if path_cost <min_cost:
                    min_cost = path_cost
                    BP = (A,match)
                    break
        M.remove(match)
    #Unite matching and spanning tree T ∪ M to form an Eulerian multigraph
    edges = union(edges,BP)
    ## 	Calculate Euler tour
    # Remove repeated vertices, giving the algorithm's output.
    mininum_tour = [ ]
    mininum_tour.append(edges[0][0])
    for i in range(0,len(edges)-1):
        mininum_tour.append(edges[i][1])
        mininum_tour.append(edges[i+1][0])
    mininum_tour.append(edges[-1][1])
    tmt = f7(mininum_tour)
    tmt.append(edges[0][0])
    custo_total = 0
    for i in range(0,len(tmt)-1,1):
        custo_total += G[tmt[i]][tmt[i+1]]
    return custo_total

if __name__ == "__main__":
    #Carrega o file tsp1 para a matriz de adjacencia
    grafo_matriz = np.loadtxt("tsp5_27603.txt",dtype='i')
    mst = prim(grafo_matriz)
    print(fides(grafo_matriz,mst))