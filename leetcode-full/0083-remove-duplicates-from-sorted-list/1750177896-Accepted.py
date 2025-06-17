# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur != None:
            next = cur.next
            if next != None :
                while next.val == cur.val :
                    print(next.val)
                    next = next.next
                    if next == None:
                        break
            
            cur.next = next
            cur = next

        return head
