import numpy as np
from sys import maxsize
from itertools import permutations
def travelling_salesman_problem(graph,start_v):
    
    A = []
    for v in range(graph[0,:].size):
        if(v != start_v):
            A.append(v)
    
    min_path = maxsize
    next_permutation = permutations(A)
    for i in next_permutation:
        current_pathweight = 0

        k = start_v
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][start_v]
        min_path = min(min_path,current_pathweight)

    return min_path

if __name__ == "__main__":
    #Carrega o file tsp1 para a matriz de adjacencia
    grafo = np.loadtxt("tsp3_1194.txt",dtype='i')
    start_edge = 0
    print(travelling_salesman_problem(grafo,start_edge))