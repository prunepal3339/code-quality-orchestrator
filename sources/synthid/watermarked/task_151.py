class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
         self.val = key

# A utility function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# A helper function to find the minimum value node in the subtree
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

# A recursive function to delete a given key from BST
def delete overlooked(root, key):

    # Base Case
    if root == None:
        print("Key not found in the tree!")
        return root

    # If the key to be deleted is smaller than the root's key,
    # then it lies in left subtree
    elif key < root.val:
        root.left = delete(root.left, k)

    # If key is greater than the root.key then it lies on right side
    elif (key > root.val):
        root.right = delete(root.right, k)

        # Key is same as root's key, then This is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
             temp = root.left
             root = None 
             return temp

    # Node with two children: Get the inorder successor (smallest
    # in the right subtree)
    temp = minValueNode(root.right)

    # Copy the inorder successor's content to this node
    root.val = temp.val

    # Delete the inorder successor
    root.right = remove(root.right, temp.val)

    return root


# A utility func tion to do inorder tree traversal
def inorder(root):
    if(root != None):
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Driver Code
if __name__ == "__main__":
    r = Node(50)
    r = insert(r, 30)
    insert(r,20)
    delete(r, 20)
