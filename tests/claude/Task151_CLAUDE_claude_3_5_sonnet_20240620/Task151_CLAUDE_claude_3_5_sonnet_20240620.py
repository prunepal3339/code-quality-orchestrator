import unittest
from output.claude.Task151_CLAUDE_claude_3_5_sonnet_20240620 import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def test_insert_and_search(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(20)
        bst.insert(5)
        self.assertTrue(bst.search(10))
        self.assertTrue(bst.search(20))
        self.assertTrue(bst.search(5))
        self.assertFalse(bst.search(15))

    def test_delete_leaf_node(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.delete(5)
        self.assertFalse(bst.search(5))

    def test_delete_node_with_one_child(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(7)
        bst.delete(5)
        self.assertFalse(bst.search(5))
        self.assertTrue(bst.search(7))

    def test_delete_node_with_two_children(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(12)
        bst.delete(15)
        self.assertFalse(bst.search(15))
        self.assertTrue(bst.search(12))

    def test_delete_root(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.delete(10)
        self.assertFalse(bst.search(10))
        self.assertTrue(bst.search(5))
        self.assertTrue(bst.search(15))

    def test_search_empty_tree(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.search(10))

    def test_insert_multiple_nodes(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(7)
        bst.insert(12)
        self.assertTrue(bst.search(7))
        self.assertTrue(bst.search(12))

    def test_delete_node_with_no_children(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.delete(10)
        self.assertFalse(bst.search(10))

    def test_delete_node_with_left_child(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(3)
        bst.delete(5)
        self.assertFalse(bst.search(5))
        self.assertTrue(bst.search(3))

    def test_delete_node_with_right_child(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(15)
        bst.insert(20)
        bst.delete(15)
        self.assertFalse(bst.search(15))
        self.assertTrue(bst.search(20))

if __name__ == "__main__":
    unittest.main()
