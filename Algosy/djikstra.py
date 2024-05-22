import heapq

def dijkstra(G, s):
    distances = [float("inf")] * len(G)
    distances[s] = 0
    priority_queue = [(0, s)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the popped node has a distance greater than the known shortest distance, skip it.
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in G[current_node]:
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
