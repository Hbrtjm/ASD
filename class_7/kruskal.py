



class Node:
    def __init__(self,id):
        self.id = id
        self.parent = None
        self.rank = 0

def find(node):
    if node.parent != node:
        node.parent = find(node.parent)  # Path compression
    return node.parent

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    
    if root1 == root2:
        return
    
    if root1.rank < root2.rank:
        root1.parent = root2
    elif root1.rank > root2.rank:
        root2.parent = root1
    else:
        root2.parent = root1
        root1.rank += 1

def kruskal(E,n):
    E = sorted(E,key=lambda d: d[2])
    V = [ Node(i) for i in range(n) ]
    e = i = 0
    A = [ None for _ in range(n-1) ]
    while e < n-1:
        u = V[E[e][0]]
        v = V[E[e][1]]
        if find(u) != find(v):
            union(u,v)
            A[e] = E[i] 
            e += 1
        i += 1
    return A