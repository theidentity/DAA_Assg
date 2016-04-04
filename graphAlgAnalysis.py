import networkx as nx
from algorithms.source import dijkstra_path, dijkstra_path_length, bellman_ford, single_source_dijkstra
from random import randint
import time
import matplotlib.pyplot as plt


DijkstraX = []
DijkstraY = []

BellmanFordX = []
BellmanFordY = []

for n in range(100,1000,100):
    D = nx.complete_graph(n)

    for (u, v) in D.edges():
        D[u][v]['weight'] = randint(0, 9)

    startTime = time.time()
    single_source_dijkstra(D,0)
    endTime = time.time()

    diff = endTime - startTime
    DijkstraX.append(n)
    DijkstraY.append(diff)

    startTime = time.time()
    bellman_ford(D,0)
    endTime = time.time()

    diff = endTime - startTime
    BellmanFordX.append(n)
    BellmanFordY.append(diff)

fig = plt.figure()
plt.plot(DijkstraX,DijkstraY,'r')
plt.plot(BellmanFordX,BellmanFordY,'b')

plt.show()
plt.close('all')
