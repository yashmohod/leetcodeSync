# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size=0
        next=head
        while next != None:
            size+=1
            next = next.next
        count=0
        next = head
        last = None
        while next!=None:
            if count == size/2:
                last.next = next
                print("Found")
            else:
                last = next
                next = next.next
        return head



        
