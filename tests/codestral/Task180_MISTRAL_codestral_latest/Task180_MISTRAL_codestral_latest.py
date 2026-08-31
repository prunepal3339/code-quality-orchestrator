class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def reparent(node, parent=None):
    if parent in node.children:
        node.children.remove(parent)
    node.children = [reparent(child, node) for child in node.children]
    return node


def print_tree(node, level=0):
    print(' ' * level + str(node.data))
    for child in node.children:
        print_tree(child, level + 1)

def test_reparent():
    # Build a sample tree:
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')

    A.children = [B, C, D]
    C.children = [E, F]

    # Test 1: After reparent, no child should have its parent in children list
    reparent(A)
    # Check B, C, D do NOT have A as child
    test1 = (A not in B.children) and (A not in C.children) and (A not in D.children)
    print("Test 1:", "pass" if test1 else "fail")

    # Test 2: Create cycle B -> A and reparent should remove it
    B.children.append(A)  # create cycle
    reparent(A)
    test2 = (A not in B.children)
    print("Test 2:", "pass" if test2 else "fail")

if __name__ == "__main__":
    test_reparent()
