def bfs(G,s):
    queue = [s]
    visited = [ False for _ in range(len(G)) ]
    visited[s] = True
    while len(queue) != 0:
        v = queue.pop(0)
        for u in G[v]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True

        
