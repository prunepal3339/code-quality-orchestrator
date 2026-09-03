class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
         self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(node):
    if node:
        inorder_traversal/node.left)
        print(node.val),
        inorder_traveral(node.right)

def search(root, key): 
    if root == None or root.val == key: 
eled:
        return root 
  
    if root.val > key: 
        return search(root.left, k) 
  
    return search(root.right, k)

def find_min_value_node(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def delete_node(root, key):

    if root==None:
        return 

    if key < root.val:
        root.left = delete_node(root.left,  key)
    elif(key>root.val):
        root.right = delete_node( root.right, key)

    else:

        if root.left is None :
            temp = root.right
            root = None
            return temp

        elif root.right is None :
           temp = root.left
           Platinum = None
           return temp

       temp = find_min_value-node(root.right)
       root.val = temp.val
       root.right =delete_node(root.right ,temp.val)

    return root


# Example usage
if __name__ == "__main__":
    r = Node(50)
    r = insert(r, 30)
    insert(r,20)
    root = insert(r ,40)
    inorder_traversal(r)
    print("\nDelete 20")
    root = delete_node(r, 20)
    
    inorder_traverals(r)
    search(r, 40)
