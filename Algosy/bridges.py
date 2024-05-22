def DFS(G, s):
    visited = [False for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    d = [0 for _ in range(len(G))]

    time = 0

    def dfs_visit(G, u):
        nonlocal time
        visited[u] = True
        time += 1
        d[u] = time
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G, v)

    for i in range(0, len(G)):
        if not visited[i]:
            dfs_visit(G, i)

    # return parent, d
    visited = [False for _ in range(len(G))]
    low = [d[v] for v in range(len(G))]

    # subgraph = [0 for _ in range(len(G))]
    def dfs_visit2(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit2(G, v)
            if visited[v] and parent[u] != v:
                low[u] = min(low[v], low[u])

    for i in range(0, len(G)):
        if not visited[i]:
            dfs_visit2(G, i)
    return low


G = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3, 4], [7], [6]]

lows = DFS(G, 0)
print(lows)
bitches = []
visited = [False for _ in range(len(G))]
for u in range(len(G)):
    if not visited[u]:
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                if lows[u] != lows[v]:
                    # visited[v] = True
                    bitches.append((u, v))

print(bitches)
