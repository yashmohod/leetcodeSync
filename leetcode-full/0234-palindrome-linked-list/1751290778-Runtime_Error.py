# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if len(po) == 1:
            return True
        po = []

        while head:
            if head.val in po:
                po.remove(head.val)
            else:
                po.append(head.val)
            head = head.next
        return len(po) == 0
