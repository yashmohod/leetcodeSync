# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        q = deque([])
        f = head
        s = head

        while f and f.next:
            q.append(s.val)
            s = s.next
            f = f.next.next
        res = -1
        while s :
            res = max(res,q.pop()+s.val)
            s = s.next
        return res

