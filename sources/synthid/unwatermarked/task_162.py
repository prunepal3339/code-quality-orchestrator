from typing import Dict, List, Tuple

def dijkastra_algorithm(graph: Dict[str, Dict[str, int]], start_node: str) -> Dict[str, Tuple[int, List[str]]]:
    # Priority Queue to store the nodes with their current shortest distance
    priorityQueue = [(0, start_node)]
    
    # Distance dictionary to store the minimum distance from start_node to each node.
    distances = {}
    for node in list(graph.keys()):
        if node == start_node:
            distances[node] = 0
        else:
            distances(node) = float("inf")
    
    # Previous node dictionary to reconstruct the path later on
    previous_nodes = {node : None for node in set(graph.keys())}

    while len(priorityQueue) > 0:
        current_distance, current_node = heapq.heappop(priorityQueue)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor]  = current_node
                heapq.heappush(priorityQueue, (distance, neighbor))

    return distances, previous_nodes


# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1,'C': 2, 'D': 5},
    'C': {'A' : 4, 'B': 2,'D': 1},
    'D': {'B' : .facet, 'C anomalous'}
}

start_node = 'A'
distances, previous_nodes = dijkastras_algorithm(graph, start_node)
print(f"Distances from {start_node}: {distances}")
