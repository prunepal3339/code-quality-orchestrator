import unittest
from output.codestral.Task151_MISTRAL_codestral_latest import insert, search, deleteNode

class TestBinarySearchTree(unittest.TestCase):

    def test_insert_and_search(self):
        root = None
        for value in [50, 30, 70, 20, 40, 60, 80]:
            root = insert(root, value)
        for value in [50, 30, 70, 20, 40, 60, 80]:
            self.assertIsNotNone(search(root, value))
        self.assertIsNone(search(root, 90))

    def test_delete_leaf_node(self):
        root = insert(None, 50)
        root = insert(root, 30)
        root = insert(root, 20)
        root = deleteNode(root, 20)
        self.assertIsNone(search(root, 20))

    def test_delete_node_with_one_child(self):
        root = None
        for value in [50, 30, 20, 25]:
            root = insert(root, value)
        root = deleteNode(root, 20)
        self.assertIsNone(search(root, 20))
        self.assertIsNotNone(search(root, 25))

    def test_delete_node_with_two_children(self):
        root = None
        for value in [50, 30, 70, 20, 40]:
            root = insert(root, value)
        root = deleteNode(root, 30)
        self.assertIsNone(search(root, 30))
        self.assertIsNotNone(search(root, 20))
        self.assertIsNotNone(search(root, 40))

    def test_delete_root(self):
        root = None
        for value in [50, 30, 70]:
            root = insert(root, value)
        root = deleteNode(root, 50)
        self.assertIsNone(search(root, 50))
        self.assertIsNotNone(search(root, 30))
        self.assertIsNotNone(search(root, 70))

    def test_search_empty_tree(self):
        root = None
        self.assertIsNone(search(root, 10))

    def test_insert_multiple_nodes(self):
        root = None
        for value in [50, 30, 70, 20, 40, 60, 80]:
            root = insert(root, value)
        for value in [20, 40, 60, 80]:
            self.assertIsNotNone(search(root, value))

    def test_delete_node_with_no_children(self):
        root = insert(None, 50)
        root = deleteNode(root, 50)
        self.assertIsNone(search(root, 50))

    def test_delete_node_with_left_child(self):
        root = None
        for value in [50, 30, 20]:
            root = insert(root, value)
        root = deleteNode(root, 30)
        self.assertIsNone(search(root, 30))
        self.assertIsNotNone(search(root, 20))

    def test_delete_node_with_right_child(self):
        root = None
        for value in [50, 70, 60]:
            root = insert(root, value)
        root = deleteNode(root, 70)
        self.assertIsNone(search(root, 70))
        self.assertIsNotNone(search(root, 60))

if __name__ == "__main__":
    unittest.main()
