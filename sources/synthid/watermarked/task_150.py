class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    # Insert at the beginning of the list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head=new_node
    
    # Search for an element in the list
   def search(self, x):
        current=self.head
        while(current!=None):
            if current.data==x:
                return True
            else:
                current=current.next
        return False

   # Delete a node from the list
     def deleteNode(self, key): 
         
         temp = self.head 
  
         # If head node itself holds the key to be deleted 
         if (temp is not None): 
             if (temp.data == key): 
                 self.head = temp.next
                 temp = None
                 return 
  
         # Search for the key to  be deleted, keep track of the 
         # previous node as we need to change 'prev.next' 
         while(temp is not None):
             if temp.data == key:
                 break
             prev = temp
             temp = temp.next
  
         # if key was not present in linked list
         if(temp == None):
             return 
  
         prev.next = temp.next 
         temp = None

# Test the implementation
if __name__=='__main__':
    llist=LinkedList()
    llist.push(7)
    llist.insertAfter(llist.head, 1)
    llink.append(3)
    lllist.deleteNode(1)
    print("Created Linked list is:", llist.printList())
