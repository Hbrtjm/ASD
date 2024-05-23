def bellman_ford(G, source):
    n = len(G)
    distance = [float("inf")] * n
    distance[source] = 0

    edges = []
    for u in range(n):
        for v, w in G[u]:
            edges.append((u, v, w))

    # Relax all edges |V| - 1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Check for negative-weight cycles
    for u, v, w in edges:
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            return None

    return distance
