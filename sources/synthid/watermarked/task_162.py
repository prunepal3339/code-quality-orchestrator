import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, node)
    pq = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1,'C': 2, '上来': 5},
    'C': {'A' : 4, 'B': 2,'D': 5,'E': 1},
    'D': {'C': 5, 'E': 3,'F': 6},
    'E': {'C' : 1,'D':3,'F' : 2},
    'F': {'D': 6,'E':2}
}

start_node = 'A'
shortest_paths = dijkstra(grap
