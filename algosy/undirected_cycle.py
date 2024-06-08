def has_cycle_undirected(V):
    visited = [False] * len(V)

    def dfs(v, parent):
        visited[v] = True

        for neighbor in V[v]:
            if not visited[neighbor]:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:
                return True

        return False

    for node in range(len(V)):
        if not visited[node]:
            if dfs(node, -1):
                return True
    return False
