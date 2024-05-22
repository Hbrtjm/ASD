def djikstra(graph,start,end):
    queue = [start]
    weights = [ None for _ in len(graph) ]
    parents = [ None for _ in len(graph) ]
    visited = [ False for _ in len(graph) ]
    while len(queue):
        current = queue[0]
        del queue[0]
        if current==end:
            print(weights[current])
            return weights[current]
        for neighbor,distance in graph[current]:
            if not visited[neighbor]:
                if weights[neighbor] is None:
                    weights[neighbor] = distance
                else:
                    if weights[neighbor] > weights[current]*distance:
                        weights[neighbor] = weights[current[distance]]
                        queue.append(neighbor)
    return None


V = []