def has_cycle(G):
    visited = [False] * len(G)
    rec_stack = [False] * len(G)

    def dfs(v):
        nonlocal visited, rec_stack
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in G[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True
        
        rec_stack[v] = False
        return False
    
    for node in range(len(G)):
        if not visited[node]:
            if dfs(node):
                return True
    return False
