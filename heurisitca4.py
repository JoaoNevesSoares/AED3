import numpy as np
import heapq
from sys import maxsize
from itertools import combinations
import random

class Graph():

    INF = maxsize
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.graph = [[0 for column in range(0,num_vertices)] for row in range(num_vertices)]
    
    def printMST(self,parent):
        for i in range(1,self.V):
            print(f"{parent[i]} - {i}   {self.graph[i][parent[i]]}")
    def minKey(self, key, mstSet):
       min = self.INF
       for v in range(self.V):
           if key[v] < min and mstSet[v] == False:
               min = key[v]
               min_index = v
       return min_index

    def prims_q(self,graph,start):
        edges = []
        weights = []
        visited_vertices = [start]
        while len(visited_vertices) < len(graph):
            moves = []
            for x in visited_vertices:
                for node in graph[x]:
                    if node[0] not in visited_vertices:
                        heapq.heappush(moves, (node[1],x,node[0]))
            next_move = heapq.heappop(moves)
            visited_vertices.append(next_move[2])
            weights.append(next_move[0])
            edges.append((next_move[1], next_move[2]))
        return edges,weights

def two_aproximative(G,weights,edges):
    custo = weights[0]
    prox_pai = edges[0][1]
    mst = 1
    visto = np.zeros(tam)
    visto[0] = 1
    while mst <tam-1:
        isnot_mst = 1
        for i in range(1,tam-1):
            if(prox_pai == edges[i][0]): #visto[i] != 1 and 
                custo+= weights[i]
                prox_pai = edges[i][1]
                visto[i] = 1
                isnot_mst = 0
                break
        if(isnot_mst):
            for i in range(0,tam-1): # (1,tam-1)
                if visto[i] == 0:
                    visto[i] = 1
                    custo += grafo_matriz[prox_pai][edges[i][1]]
                    prox_pai = edges[i][1]
                    break
        mst +=1
    custo += grafo_matriz[prox_pai][0]
    return custo

if __name__ == "__main__":
    #Carrega o file tsp1 para a matriz de adjacencia
    grafo_matriz = np.loadtxt("tsp5_27603.txt",dtype='i')
    tam = grafo_matriz[0,:].size
    adj = [[0 for column in range(0,tam)] for row in range(tam)]
    for i in range(0,tam):
        for j in range(0,tam):
            adj[i][j] = (j,grafo_matriz[i][j])
    start_edge = 0
    g = Graph(tam)
    g.graph = grafo_matriz
    edges, weights = g.prims_q(adj,start_edge)
    print(two_aproximative(grafo_matriz,weights=weights,edges=edges))