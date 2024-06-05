# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        n=0

        cur = head

        while cur != None:
            cur = cur.next
            n+=1
        
        
        count = 1
        cur = head
        last = None

        while cur!=None:
            if count == n/2:
                if last == None:
                    last = cur
                    cur = cur.next
                else:
                    temp = cur 
                    cur = cur.next
                    temp.next = last 
                    last = temp
            else:
                cur = cur.next
                count+=1

        lg=head.val + last.val
        count=1
        while count != n/2:
            if lg<head.val + last.val:
                lg = head.val + last.val
            head = head.next
            last = last.next
            count+=1

        return lg
