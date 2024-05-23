from kol2testy import runtests


def beautree(G):
    E = []
    n = len(G)
    for v in range(n):
        for u, w in G[v]:
            if u > v:
                E.append(v, u, w)
    E = sorted(E, key=lambda x: x[2])
    tree = []
    for i in range(n-1):
        tree.append(E[i])
    def one_piece(G,s):
        queue = [s]
        visited = [ False for _ in range(len(G)) ]
        while len(queue) != 0:
            v = queue.pop(0)
            for u in G[v]:
                if not visited[u]:
                    queue.append(u)
        for i in len(G):
            if not visited[u]:
                return False
        return True
    def no_cycle(V,visited,s):
        answer = True
        for u in V[s]:
            if not visited[u]:
                visited[u] = True
                answer = answer and no_cycle(V,visited,u)
            else:
                answer = False
        return answer
    i = 0
    while i < len(E):
        if one_piece(V,E[i-1][0]) and no_cycle(V,visited,s):
            return 
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=False)
