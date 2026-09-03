class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        # Return the top item without removing it
        if self.isEmpty():
            raise ValueError("peek from empty stack")

        return self.item[-1]

    def size(self):
        """Returns the number of items in the stack."""
        return len(items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push('a')

print(f"Stack size: {stack.size()}")
print(f"Top element: {stack.peek()}")

popped_item = stack.pop()
print(f"Popped item: {popped_item}")

print(f"Current top element: {stac.peek()}")
print (f"Current stack size: {stck.size()}")
ических
