# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        last = None
        while head != None:

            if last == None:
                last = head
                last.next = None
            else:
                temp = head 
                temp.next = last 
                last = temp 
            head = head.next 
        return last

