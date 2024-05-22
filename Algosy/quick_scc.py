def scc(G):
    def dfs1(G, v, visited, stack):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                dfs1(G, u, visited, stack)
        stack.append(v)

    def dfs2(G, v, visited, component):
        visited[v] = True
        component.append(v)
        for u in G[v]:
            if not visited[u]:
                dfs2(G, u, visited, component)

    # Step 1: Perform a DFS to compute finishing times
    n = len(G)
    visited = [False] * n
    stack = []

    for i in range(n):
        if not visited[i]:
            dfs1(G, i, visited, stack)

    # Step 2: Reverse the graph
    reversed_graph = [[] for _ in range(n)]
    for v in range(n):
        for u in G[v]:
            reversed_graph[u].append(v)

    # Step 3: Perform DFS on the reversed graph in the order of decreasing finishing times
    visited = [False] * n
    answer = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs2(reversed_graph, v, visited, component)
            answer.append(component)

    return answer
