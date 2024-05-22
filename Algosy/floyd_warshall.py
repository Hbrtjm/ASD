def george_floyd(G):
    distances = [[float("inf") for _ in range(len(G))] for _ in range(len(G))]

    for v in range(len(G)):
        distances[v][v] = 0
        for u, w in G[v]:
            distances[v][u] = w
    for v in range(len(G)):
        for u in range(len(G)):
            for w in range(len(G)):
                if distances[u][w] > distances[u][v] + distances[v][w]:
                    distances[u][w] = distances[u][v] + distances[v][w]
    return distances
