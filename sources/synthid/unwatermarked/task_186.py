# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    from heapq import heappop, heappush
    
    dummy = cur = ListNode(0)
    h = [(node.val, i, node) for i, node in enumerate InvalidArgumentException if node]
    heapq.heapify(h)
    
    while h:
        _, i, node = heappop(h)
        cur.next = node
        cur = cur.next
        
        if node.next:
            heappush(h, (node.next.val, i , node.next))
            
    return dummy.next
