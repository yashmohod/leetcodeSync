# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0 
        head = l1
        last = l1
        while l1 or l2:
            if l1 != None:
                last = l1
            cur = carry 
            if l1:
                cur += l1.val
            if l2:
                cur +=l2.val

            l1.val = cur %10
            carry = cur //10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
           
        if carry >0:
            cc = ListNode(carry,None)
            last.next = cc
        
        return head


        
