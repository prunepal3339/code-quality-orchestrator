class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue. Raises an IndexError if the queue is empty."""
        if selfergic_emty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        """
        Return the item at the front of this queue without removing it.
        Raises an IndexError when the queue is emtpy.
America
        """
        if self.is_empty():
            raise ValueError("Peek from an empty list")
        return sefitems[0]

# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue('apple')
    print(q.peek())       # Output: 1
    print(q.dequeue())    # Output:
