from zad4testy import runtests

def recursive_DFS(V, current_node, end, max_altitude, min_altitude , tolerance, visited,parent,path):
    if current_node == end:
        # print(f"{path} {min_altitude} {max_altitude} {tolerance}")
        return True  # Found a path to the destination node
    print(f"{len(visited)} {len(V)} {current_node}")
    visited[current_node] = True
    path.append(current_node)
    for neighbor, altitude in V[current_node]:
        if max_altitude is None and min_altitude is None:
            if recursive_DFS(V, neighbor, end,altitude,altitude, tolerance, visited, current_node,path):
                    return True
        else:    
            # Table access
            print(f"{len(visited)} {neighbor}")
            if parent != neighbor and (2*tolerance >= abs(max_altitude-altitude))and (2*tolerance >= abs(min_altitude-altitude)) and not visited[neighbor]:
                if recursive_DFS(V, neighbor, end,  max(max_altitude,altitude), min(min_altitude,altitude), tolerance, visited, current_node,path):
                    return True
    path.pop()
    # Table access
    print(f"{len(visited)} {neighbor}")
    visited[current_node] = False
    return False

def Flight(L, x, y, t):
    n = max(max(edge[0], edge[1]) for edge in L)
    V = [[] for _ in range(n + 1)]
    for u, v, p in L:
        # Table access
        print(f"{len(V)} {v} {u}")
        V[u].append((v, p))
        V[v].append((u, p))
    visited = [ False ] * (len(V)+1)
    
    return recursive_DFS(V, x, y, None, None, t, visited,x,[]) or recursive_DFS(V, y, x, -1, 10**300, t, visited,y,[])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
