class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def reparent_tree(root, new_root):
    if root == new_root:
        return root
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node == new_root:
            return node
        queue.extend(node.children)
    return None

def test_reparent_tree():
    root = Node(0)
    root.children = [Node(1), Node(2), Node(3)]
    root.children[0].children = [Node(4), Node(5)]
    root.children[1].children = [Node(6), Node(7)]
    root.children[2].children = [Node(8), Node(9)]

    def find_node_by_value(node, value):
        if node.value == value:
            return node
        for c in node.children:
            found = find_node_by_value(c, value)
            if found:
                return found
        return None

    new_root_node = find_node_by_value(root, 6)
    result = reparent_tree(root, new_root_node)
    print("Test 1:", "pass" if result is not None and result.value == 6 else "fail")
    print("Test 2:", "pass" if result is new_root_node else "fail")

    result_root = reparent_tree(root, root)
    print("Test 3:", "pass" if result_root is root else "fail")

    non_existent = Node(99)
    result_none = reparent_tree(root, non_existent)
    print("Test 4:", "pass" if result_none is None else "fail")

if __name__ == "__main__":
    test_reparent_tree()
