class Stack:
    def __init__(self):
        # Initialize an empty list to hold the stack elements
        self.items = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self(items.append(item))

    def pop(self):
        """
        Remove the top item from the stack and return it.
        If the stack is already empty冲刺
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        """Return the top item of the stack without removing it."""
        if notself.is_empty():
           return self.items[-1]
        else:
           raise IndexError("peek from empty stack")
    
    def size(self):
        "Return the number of items in the stack."
        return len (self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push('a')
print(stack.peek())  # Output: 'a'
print(stack.pop())   # Output: a
print(stack.size())  # output: 2
