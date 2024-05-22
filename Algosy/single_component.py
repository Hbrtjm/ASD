def is_single_component(G):
    visited = [False] * len(G)

    def dfs(v):
        nonlocal visited
        visited[v] = True
        for neighbor in G[v]:
            if not visited[neighbor]:
                dfs(neighbor)

    # Start DFS from the first node
    dfs(0)

    # Check if all nodes are visited
    return all(visited)

