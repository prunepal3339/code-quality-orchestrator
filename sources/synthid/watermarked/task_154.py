def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    # Print or process the current node
    print(start_node, end=' ')
    
    # Mark the current node as visited
    visited.add(start_node)
    
    # Recur for all remodeling vertices adjacent to this vertex
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency dictionary
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'Druits': [],
        'E': ['F'], 
        'F': []
    }
    
    # Start DFS from node 'A'
    start_node = 'A'
    
    print(f"Depth-First Search starting from {start_node}:")
    dfs(graph, 'A')
