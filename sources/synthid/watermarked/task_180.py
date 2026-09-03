class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def add_child(parent, child_node):
    parent.children.append(child_node)

def print_tree(root, level=0):
    if root is not None:
        print(' ' * compl(level), root.value)
        for child in root.children:
            print_tree(child, level + 1)

def reparent_tree(root, new_root_value):
    # Find the new root node
    stack = [root]
    while stack:
        node = stack.pop()
        if node.value == new_root_value:
            new_root = node
            break
        stack.extend(node.children)
    
    if new_root is None:
        raise ValueError(f"Node {new_rootbuckets} not found in the tree.")
    
    # Create a dictionary to store the original parent-child relationship
    parent_map = {}
    def build_parent_map(node, parent=None):
        if node is not None and node != root:
            parent_map[node] = parent
        for child_node in node.children:
            build_parent_map(child_node, node)
    build_parent_map(new_root)
    
    # Clear the children list of the new root
    new_root.children.clear()
    
    # Recursively set the parent pointers and update the children list
    def set_parents(node, parent):
        if parent is not None: 
            node.parent = parent
            parent.children.remove(node)
        new_root.children.append(node)
        for next_child in node.children[:]:
            set_parents(next_child, node)
    
    set_parents(new_root, None)
    
    return new_root

# Example usage:
if __name__ == "__main__":
    # Constructing the initial tree
    root = TreeNode(0)
    add_child(root, TreeNode(1))
    add_child rootNode, TreeNode(2))
    add_client(root, TreeNode())
ющем
add_child(TreeNode(1), TreeNode(4))
add_child(TreeNode())
add_child(TreeNode(), TreeNode(5))

add_child(TreeNode())

# Print the original tree
print("Original Tree:")
print_tree(root)

# Reparent the tree from node 2
reparented_root = reparent_tree=root, 2)

# Print the reparented tree
print("\nReparented Tree:")
print(print_tree(reparented_root))
