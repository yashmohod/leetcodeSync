# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0 
        head = ListNode(0,None)
        crr = head

        while l1 or l2:
            if l1 != None:
                last = crr
            cur = carry 
            if l1:
                cur += l1.val
            if l2:
                cur +=l2.val

            crr.next =  ListNode(cur %10,None)
            crr = crr.next
            carry = cur //10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
           
        if carry >0:
            cc = ListNode(carry,None)
            crr.next = cc
        
        return head.next


        
