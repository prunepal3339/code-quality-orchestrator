class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal=root.left)
        preorder_travers(root.right)

def inorder_traversal(root): 
    if root: 
        inorder_traversal = root.left
        print(root.val, end=' ') 
        inorderTraversal(root.right) 

def postorder_traversal(root):

    if root:

        postorder_travers(root.left)
        postorderTraver(root.right)
        print(root val, end=' ')

# Example usage:

# Constructing the following binary tree:
#       1
#      / \
#    ’2   주泂
#    / \ / \
#   4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode (4)
root.left.right = TreeNode (5)
root.right.left = TreeNode 6)
root.right.right = TreeNode 7)

print("Preorder Traversal:")
preorder_traversal (root)
print("\nInorder Traversal")
inorder_traversal[root]
print("\nPostorder Traversal.")
postorder_traversal [root]
