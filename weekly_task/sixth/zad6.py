'''
======================================================================================================================================================================================================================|
|                                                                                                                                                                                                                     |
|   Autor zadania: Hubert Miklas                                                                                                                                                                                      |
|   Złożoność czasowa algorytmu: O(V^3)                                                                                                                                                                               |
|   Złożoność pamięciowa algorytmu: O(V^2)                                                                                                                                                                            |
|                                                                                                                                                                                                                     |
|   Opis algorytmu:                                                                                                                                                                                                   |
|   Dla każdej krawędzi zapisujemy dwie zmienne - jedna reprezentuje ścieżkę, dla której ostatnio użyto nie butów i drugą, w której buty zostaly użyte. Idziemy po grafie i zapamiętujemy poprzedni stan przejścia,   |
|   jeżeli dwumilowe buty były ostatnio użyte, to do relaksacja jest względem indeksu 0 dla krawędzi v. Jeśli nie to używamy butów i zapisujemy w 1-szym indeksie wartość dla przejścia przy użyciu butów. Dla każdego|
|   sąsiada v przeskakujemy dwumilowymi butami. Na koniec zwracamy minimalny dystans w wierzchołku końcowym, jeśli ścieżka nie istnieje, zwrócimy inf                                                                 |  
|                                                                                                                                                                                                                     |
======================================================================================================================================================================================================================|
'''

from zad6testy import runtests
import heapq

def jumper(G, s, w):
    n = len(G)
    distances = [[float('inf'), float('inf')] for _ in range(n)]
    distances[s][0] = 0
    queue = [(0, s, 0)] 
    while queue:
        current_dist, u, state = heapq.heappop(queue)
        if current_dist > distances[u][state]:
            continue
        for v in range(n):
            if G[u][v] > 0:
                new_dist = current_dist + G[u][v]
                if new_dist < distances[v][0]:
                    distances[v][0] = new_dist
                    heapq.heappush(queue, (new_dist, v, 0))
        if state == 0:
            for intermediate in range(n):
                if G[u][intermediate] > 0:
                    for v in range(n):
                        if G[intermediate][v] > 0 and v != u:
                            jump_cost = max(G[u][intermediate], G[intermediate][v])
                            new_dist = current_dist + jump_cost
                            if new_dist < distances[v][1]:
                                distances[v][1] = new_dist
                                heapq.heappush(queue, (new_dist, v, 1))
    return min(distances[w][0], distances[w][1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )