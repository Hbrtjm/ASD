from egzP3btesty import runtests 
from queue import PriorityQueue

def find(x,p):
    while p[x] != x:
        x = p[x]
    return x 

def union(x,y,p,rank):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def kruskal( G ):
    E = []
    rank = [ 0 for _ in range(len(G)) ]
    for e in E:
        u,v,w = e
        if find(u,p) != find(v,p):
            union(u,v,p,rank)
            answer.append(e)


def lufthansa ( G ):
    
    return 0 

runtests ( lufthansa, all_tests=True )