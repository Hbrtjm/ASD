def toposort(G):
    answer = []
    visited = [False for _ in range(len(G))]

    def dfs(G, current):
        nonlocal answer, visited
        visited[current] = True
        for u in G[current]:
            if not visited[u]:
                dfs(G, u)
        answer.append(current)

    for i in range(len(G)):
        if not visited[i]:
            dfs(G, i)
    return answer
