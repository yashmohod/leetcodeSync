# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        oddFirst = None
        oddLast=None
        evenFirst=None
        evenLast=None
        cur = head
        count =1
        while cur != None:
            print(cur.val)
            if count %2 ==0:
                if evenLast == None:
                    evenLast = cur
                    evenFirst = cur
                else:
                    evenLast.next = cur 
                    evenLast = cur
            else:
                if oddLast == None:
                    oddLast = cur
                    oddFirst = cur
                else:
                    oddLast.next = cur 
                    oddLast = cur
            cur = cur.next
            count +=1
        oddLast.next = evenFirst
        evenLast.next = None
        return oddFirst
