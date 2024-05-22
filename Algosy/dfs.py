def dfs(G, start):
    visited = [False] * len(G)
    
    def dfs_visit(v):
        nonlocal visited
        visited[v] = True
        print(v, end=' ')
        for u in G[v]:
            if not visited[u]:
                dfs_visit(u)
    
    dfs_visit(start)
