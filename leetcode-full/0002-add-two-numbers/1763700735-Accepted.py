# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        con =res
        crr=0

        while l1 or l2 or crr:
            r = 0 
            if l1:
                r+=l1.val
                l1 = l1.next
            if l2:
                r+=l2.val
                l2=l2.next
            r+=crr
            crr = r //10
            con.next = ListNode(r%10)
            con = con.next

        return res.next
            


