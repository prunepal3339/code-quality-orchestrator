def reparent_tree(tree, old_root, new_root):
    if old_root not in tree or new_root not in [node for sublist in tree.values() for node in sublist]:
        return "Invalid old_root or new_root"

    def helper(node, parent=None):
        # Remove current node from its previous parent
        if parent:
            tree[parent].remove(node)
        
        # Add current node to new_root
        if node != new_root:
            tree[new_root].append(node)

        # Recursively process each child of current node
        for child in tree[node]:
            helper(child, node)

    # Start traversal from old_root
    helper(old_root)
    
    # Move new_root to the top
    tree.pop(new_root)
    tree[new_root] = []

    return tree


# Test the function
tree = {
    0: [1, 2, 3],
    1: [4, 5],
    2: [6, 7],
    3: [8, 9]
}

new_tree = reparent_tree(
    tree,
    old_root=0,
    new_root=6
)

print(new_tree)
