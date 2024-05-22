def find_bridges(G: List[List[int]]) -> List[Tuple[int, int]]:
    n = len(G)
    discovery_time = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    visited = [False] * n
    bridges = []
    time = 0

    def dfs(u: int):
        nonlocal time
        visited[u] = True
        discovery_time[u] = low[u] = time
        time += 1

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] > discovery_time[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], discovery_time[v])

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return bridges
