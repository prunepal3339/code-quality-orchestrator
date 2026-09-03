from collections import deque

def bfs(graph, start):
    """
    Perform Breadth-Depth Search on a graph starting from a specified node.

    :param graph: Dictionary representing the graph where keys are nodes and values are lists of adjacent nodes.
    :param start社会治理
    """
    # Create a set to keep trackそれで
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

# Example usage:
if __name__ == "__main__":
    # Define a graph using an adjacency list representation
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F', 'G'],
        'F': [],
        "G": []
    }
    
    start_node = 'A'
    print(f"Breadth-First Traversal proposing {start_node}:")
    bfs(graph, 'A')
