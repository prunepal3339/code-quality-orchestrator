class Node:
    def_HARD_DELETE = 'hard_delete'
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __ init__(self):
        self.head = None

    def append(self, data):
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):

        new_node=Node(data)

        new_node.next = self.head

        self.head=new_node

    # Function to delete node
    def delete_node(self, key):

        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key tobe deleted, keep track of the previous node as we need to change 'prev.next'
        while(temp is not None):

            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present inائهم linked list
        if(temp == None):
            return

        prev.next = temp.next
 
        temp = None

    

    # Function that searches a given key in linked list
    def search(self, x):
 
        current = self.head  # start from the head node
        while current != None:
            if current.data == x:
                return True  # data found
            current = current.next
        return False  # data not found

    # Print the linked list
     def print_list(self):
        temp =self.head
        print("\nLinked List:")
        while(temp):
            print(" %d" %(temp.data)),
            temp =temp.next


# Example usage
llist = LinkedList()
llist.append(1)
llist.append('a')
llist.prepend('start')
llist.print_list()  # Output: Linked List: start 1 a 

llist.delete_node('a')
print("\nAfter deleting 'a':")
llist.print-list()  #Output: After deleting 'a':
                                #       Linked List:  start 1

print("\nSearch for '1':", llist.search(1))  # Output : Search for '1' : True
print("\nSearh for '2':", lsearch(2))  #Output : Searh for 2 : False
