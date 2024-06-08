def bfs_cycle(G,s):
    visited = [ False for _ in range(len(G)) ]
    queue = [s]
    parent = [ None for _ in range(len(G)) ]
    parent[s] = s
    while len(queue) != 0:
        v = queue.pop(0)
        for u in G[v]:
            if not visited[u]:
                queue.append(u)
                parent[u] = v
                visited[u] = True
            elif parent[v] != u:
                return False
    return True
                
