def dfs(graph, start_node):
    # Create a set to keep track of visited nodes
    visited = set()
    
    # Define a recursive function to perform DFS
    def dfs_recursive(node):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                dfs_recursive(neighbor)
    
    # Start DFS from the start_node
    dfs_recursive(start_node)

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'], 
        'F': []
    }
    
    # Specify the starting node
    start_node = 'A'
    
    # Perform DFS
    print(f"Depth-First Search starting from {start_node}:")
    dfs(graph, 'A')
