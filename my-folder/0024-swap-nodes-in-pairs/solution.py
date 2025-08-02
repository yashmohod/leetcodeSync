# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        d = ListNode(0,head)

        p,c = d,head

        while c and c.next:

            np = c.next.next
            s = c.next 

            s.next = c 
            c.next = np 
            p.next = s

            p = c 
            c = np 
        

        return d.next 
