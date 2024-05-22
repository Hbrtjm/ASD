def scc(G):
    reversed = [[] for _ in range(len(G))]
    time = 0
    processed_time = [None for _ in range(len(G))]
    for v in range(len(G)):
        for u in G[v]:
            reversed[u].append(v)

    def dfs(G, current):
        nonlocal time, visited
        time += 1
        for u in G[current]:
            if not visited[u]:
                dfs(G, u)
        processed_time[current] = time

    visited = [False for _ in range(len(G))]

    for i in range(len(G)):
        if not visited[i]:
            dfs(G, i)

    def dfs2(reversed, current, component):
        nonlocal visited
        for u in G[current]:
            if not visited:
                component.append(u)

    answer = []
    anstable = [(processed_time[i], i) for i in range(len(G))]
    anstable = sorted(anstable, key=lambda x: x[0])
    visited = [False for _ in range(len(G))]
    for i in range(len(G)):
        if not visited[i]:
            component = []
            dfs2(reversed, i, component)
            answer.append(component)
    return answer
