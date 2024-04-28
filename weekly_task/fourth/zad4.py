from time import sleep
from zad4testy import runtests

def invalid(a,n):
    return a < 0 or a >= n

def recursive_DFS(V, current_node, end, max_altitude, min_altitude , tolerance, visited,parent,path):
    if current_node == end:
        return True # Found the destination node
    visited[current_node] = True
    path.append(current_node)
    for neighbor, altitude in V[current_node]:
        if max_altitude is None and min_altitude is None:
            if recursive_DFS(V, neighbor, end,altitude,altitude, tolerance, visited, current_node,path):
                    return True
        else:
            # Check if that flight placement exists
            if parent != neighbor and (2*tolerance >= abs(max_altitude-altitude))and (2*tolerance >= abs(min_altitude-altitude)) and not visited[neighbor]:
                if recursive_DFS(V, neighbor, end,  max(max_altitude,altitude), min(min_altitude,altitude), tolerance, visited, current_node,path):
                    return True
    path.pop()
    visited[current_node] = False
    return False


def Flight(L, x, y, t):
    n = max(max(edge[0], edge[1]) for edge in L)
    V = [[] for _ in range(n + 2)]
    for u, v, p in L:
        V[u].append((v, p))
        V[v].append((u, p))
    visited = [ False ] * (len(V))

    # return DFS_visit(L, x,y,visited,t,0,None,None)    
    return recursive_DFS(V, x, y, None, None, t, visited,x,[]) # or recursive_DFS(V, y, x, None, None, t, visited,y,[])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )


sleep(100)