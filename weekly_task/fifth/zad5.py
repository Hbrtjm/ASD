'''
======================================================================================================================================================================================================================|
|                                                                                                                                                                                                                     |
|   Autor zadania: Hubert Miklas                                                                                                                                                                                      |
|   Złożoność czasowa algorytmu: O(E * log V)                                                                                                                                                                         |
|   Złożoność pamięciowa algorytmu: O(V + E)                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
|   Opis algorytmu:                                                                                                                                                                                                   |
|   Szukam najkrótszej scieżki do najbliższej osobliwości. W takim razie do każdej innej osobliwości minimalna odleglość od punktu startodego do tej osobliwości jest równa wcześniej wyliczonej min_warp_distance.   |
|   Później poszukuję ścieżki standardowo djikstrą zaczynając od punktu startowego. W przypadku napotkania osobliwości distance[current] = min_warp_distance. Jeśli żadna ścieżka nie została odnaleziona, to musimy  |
|   jeszcze sprawdzić nieodwiedzone osobliwości, bo w tym przypadku graf nie jest spójny. W przypadku, gdy ścieżka nie istnieje zwracamy None.                                                                        |
|                                                                                                                                                                                                                     |
======================================================================================================================================================================================================================|
'''
from zad5testy import runtests
import heapq # legalny import, bo kopce były w części I
from collections import deque # Legalny import

def find_warp(V, a, flags):
    pq = []
    heapq.heappush(pq, (0, a))
    min_warp_distance = float('inf')
    distances = [float('inf')] * len(V)
    distances[a] = 0
    visited = [ False ] * len(V)
    # iterations = 0
    while pq:
        current_distance, current = heapq.heappop(pq)
        if visited[current]:
            continue
        visited[current] = True
        # iterations += 1
        for neighbor, weight in V[current]:
            if visited[neighbor]:
                continue
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
        if flags[current]:
            min_warp_distance = min(min_warp_distance, current_distance)
    # print(iterations)
    return min_warp_distance if min_warp_distance != float('inf') else None

def find_route(V, a, b, flags, warp_distance,visited,start):
    queue = deque([a])
    distances = [float('inf')] * len(V)
    distances[a] = start
    visited[a] = True
    while queue:
        current = queue.popleft()
        for neighbor, distance in V[current]:
            if flags[neighbor] and warp_distance is not None:
                new_distance = warp_distance
            else:
                new_distance = distances[current] + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                queue.append(neighbor)
    return distances[b] if distances[b] != float('inf') else None

def spacetravel(n, E, S, a, b):
    V = [[] for _ in range(n)]
    visited = [False] * len(V)
    flags = [False] * n
    for u, v, w in E:
        V[u].append((v, w))
        V[v].append((u, w))
        if u in S:
            flags[u] = True
        if v in S:
            flags[v] = True
    warp_distance = find_warp(V, a, flags)
    # print(warp_distance)
    ans = find_route(V, a, b, flags, warp_distance,visited,0)
    if ans is None:
        # If the graph is not a singular connected component, search different warps 
        for warp in S:
            if not visited[warp]:
                ans = find_route(V,warp,b,flags,warp_distance,visited,warp_distance)
            if ans is not None:
                break
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )