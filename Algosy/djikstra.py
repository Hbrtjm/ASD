import heapq


def djikstra(G, s):
    distances = [float("inf") for _ in range(len(G))]
    distances[s] = 0
    queue = [s]
    while len(queue) != 0:
        current = heapq.heappop(queue)
        for u, w in G[current]:
            if distances[u] > distances[current] + w:
                distances[u] = distances[current] + w
                heapq.heappush(queue, (distances[u], u))
    return distances
