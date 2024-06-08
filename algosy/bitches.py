def bridges(G):
    low = [float("inf") for _ in range(len(G))]
    time = 0
    visited = [False for _ in range(len(G))]
    visit_time = [float("inf") for _ in range(len(G))]
    parent = [i for i in range(len(G))]

    def dfs(G, v):
        nonlocal visit_time, visited, parent, low, time
        time += 1
        visit_time[v] = time
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                dfs(G, u)
        for u in G[v]:
            if u != parent[v]:
                low[v] = min(low[v], low[u])

    for i in range(len(G)):
        if not visited[i]:
            dfs(G, i)
