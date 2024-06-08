"""
----------------------------------------------------------------------------------------------------------------
|
|   Autor zadania: Hubert Miklas
|   Złożoność czasowa: O(ElogV)
|   Złożóność pamięciowa: O(V + E) (Na dodatkowe przetłumaczenie grafu)
|   
|   Opis algorytmu: Najpierw przekładam graf z reprezentacji krawędziowej na listę sąsiedztwa w złożoności czasowej O(E) i 
|   zajmuję dodatkowo O(V + E) miejsca. Później wojownik idzie po najkrótszych ścieżkach, jeśli jest zbyt 
|   zmęczony, żeby iść dalej, dodaje do czasu swojej drogi odpoczynek w schronisku.
|   Przechodzimy tutaj algorytmem djisktry, do trasy dodaję 8 godzin, jeżeli wojownik
|   musiał odpocząć (To jest przejście z aktualnego wierzchołka do następnego zajmuje więcej niż 16 godzin).
|   Algorytm wykonuje się w złożoności czasowej O(Elog(V)) i zużywa O(V) dodatkowej pamięci
|   na tablicę odległości. Algorytm jest poprawny, ponieważ jest to zmodyfikowana djikstra, której poprawność
|   została udowodniona na wykładzie. Bierzemy pod uwagę drogę, która zawiera najmniejszą ilość zmęczenia i długość
|   podróży.
|
----------------------------------------------------------------------------------------------------------------
"""

from kol2testy import runtests
from collections import deque

def warrior(G, s, t):
    n = 0
    for u, v, _ in G:
        n = max(n, u, v)
    V = [[] for _ in range(n + 1)]
    for u, v, w in G:
        V[u].append((v, w))
        V[v].append((u, w))

    distances = [[float('inf') for _ in range(17)] for _ in range(n + 1)]
    distances[s][0] = 0
    queue = deque([(s, 0)])  # (current node, hours walked without rest)

    while queue:
        v, current_tired = queue.popleft()
        current_distance = distances[v][current_tired]
        
        for u, distance in V[v]:
            new_tired = current_tired + distance
            new_distance = current_distance + distance
            if new_tired > 16:
                new_tired = distance
                new_distance += 8
            if distances[u][new_tired] > new_distance:
                distances[u][new_tired] = new_distance
                if new_tired == distance:
                    queue.append((u, new_tired))  # Prioritize rest state to be checked later
                else:
                    queue.appendleft((u, new_tired))  # Continue without rest, prioritize

    ans = float('inf')
    for i in range(17):
        ans = min(ans, distances[t][i])
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(warrior, all_tests=True)
