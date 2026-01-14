# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        o = head
        eh =head.next
        e = head.next
        t = e.next
        c = 1

        while t :
            tmp = t.next
            if c % 2 :
                o.next = t
                o = t 
            else:
                e.next = t 
                e = t
            c+=1
            t = tmp
        
        e.next = None      # IMPORTANT: terminate even list
        o.next = eh        # stitch odd tail to even head
        return head
