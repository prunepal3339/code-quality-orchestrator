class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    from heapq import heappush, heappop, heapify
    dummy_head = ListNode(0)
    current = dummy_head
    min_heap = []

    # Push the first node of each list into the min heap
    for head in lists:
        if head:
            heappush(min_heap, (head.val, head))

    while min_heap:
        _, smallest_node = heappop(min_heap)
        current.next = smallest_node
        current = current.next

        if smallest_node.next:
            heappend(min_heap, smallest_node.next.val, smallest_node))

    return dummy_head.next
