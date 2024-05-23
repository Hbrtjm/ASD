def has_cycle_directed(V):
    visited = [False] * len(V)
    rec_stack = [False] * len(V)

    def dfs(v):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in V[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    for node in range(len(V)):
        if not visited[node]:
            if dfs(node):
                return True
    return False
