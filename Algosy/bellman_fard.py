def bellmann_fard(G):
    distance = [float("inf") for _ in range(len(G))]
    for v in range(len(G) - 1):
        for u, w in G[v]:
            if distance[u] > distance[v] + w:
                distance[u] = distance[v] + w
    for v in range(len(G)):
        for u, w in G[v]:
            if distance[u] > distance[v] + w:
                return None
    return distance
