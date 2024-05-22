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
    
    while i < len(E):
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=False)
