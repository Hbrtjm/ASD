def floyd_warshall(G):
    n = len(G)
    distances = [[float("inf") for _ in range(n)] for _ in range(n)]

    for v in range(n):
        distances[v][v] = 0
        for u, w in G[v]:
            distances[v][u] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances
