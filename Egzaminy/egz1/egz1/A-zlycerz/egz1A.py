from egz1Atesty import runtests
from heapq import heappop, heappush

def find_path_robbing_ith(G, V, s, t, r, castle, distances):
    queue = [(0, s, False)]
    distances[castle][s] = 0
    while len(queue):
        current_distance, current, stolen = heappop(queue)
        if distances[castle][current] < current_distance:
            continue
        if current == castle and not stolen:
            current_distance -= V[current]
            stolen = True
        for neighbor, distance in G[current]:
            if stolen:
                distance += r
            next_distance = current_distance + distance
            if next_distance < distances[castle][neighbor]:
                distances[castle][neighbor] = next_distance
                heappush(queue, (next_distance, neighbor, stolen))
    return distances[castle][t]

def gold(G, V, s, t, r):
    answer = float('inf')
    n = len(V)
    costs = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        answer = min(answer, find_path_robbing_ith(G, V, s, t, r, i, costs))
    
    return answer

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=False)
