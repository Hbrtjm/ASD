def topological_sort(current,visited,stack):
    ans = []

    return None

def whole_topological_sort(V):
    visited = [ False for _ in len(V) ]

    stack = []

    for vertex in range(len(V)):
        if not visited[vertex]:
            topological_sort(vertex,visited,)
    stack.reverse()
    return stack