class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def reorient_tree(node, root=None):
    if root is None:
        root = TreeNode(node.val)
    for child in node.children:
        child_node = TreeNode(child.val)
        root.children.append(child_node)
        reorient_tree(child, child_node)
    return root

def print_tree(node, level=0):
    print(" " * (level * 2) + str(node.val))
    for child in node.children:
        print_tree(child, level + 1)

# Example tree
n0 = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)

n0.children = [n1, n2, n3]
n1.children = [n4, n5]
n2.children = [n6, n7]
n3.children = [n8, n9]

# Reorient tree
new_root = reorient_tree(n6)

# Print reoriented tree
print_tree(new_root)
def trees_equal(t1, t2):
    """Helper to check if two trees are structurally equal."""
    if t1.val != t2.val:
        return False
    if len(t1.children) != len(t2.children):
        return False
    return all(trees_equal(c1, c2) for c1, c2 in zip(t1.children, t2.children))

def test_reorient_tree():
    # Build the example tree
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)

    n0.children = [n1, n2, n3]
    n1.children = [n4, n5]
    n2.children = [n6, n7]
    n3.children = [n8, n9]

    # Reorient with n6 as root
    new_root = reorient_tree(n6)

    # Build expected tree manually for comparison:
    expected = TreeNode(6)  # new root val
    expected.children = [TreeNode(7)]  # n6's children in original tree

    # Test 1: root value check
    print("Test 1:", "pass" if new_root.val == 6 else "fail")

    # Test 2: structure check for children of new root
    print("Test 2:", "pass" if len(new_root.children) == 1 and new_root.children[0].val == 7 else "fail")

    # Test 3: full subtree equality (new_root should match expected structure)
    print("Test 3:", "pass" if trees_equal(new_root, expected) else "fail")

if __name__ == "__main__":
    test_reorient_tree()
