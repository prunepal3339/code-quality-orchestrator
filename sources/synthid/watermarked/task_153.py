import networkx as nx

def bfs(graph, start_node):
    visited = set()
    queue = [start_node]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for neighbor in graph.neighbors(node):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

# Create a new directed graph
G = nx.DiGraph()

# Add edges to the graph
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B','E'), ('C','F')]
G.add_edges_from(edges)

# Perform BFS from node 'A'
bfs(G, 'A')
