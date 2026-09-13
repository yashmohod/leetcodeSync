# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h = [(node.val,i,node) for i,node in enumerate(lists) if node]
        heapq.heapify(h)
        res = ListNode()
        next = res
        while h:
            val,i,node = heapq.heappop(h)
            next.next = node
            next = node
            if node.next:
                heapq.heappush(h,(node.next.val,i,node.next))
        return res.next







