# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        nxt = head.next

        def gcd(a,b):
            
            if a % b == 0:
                return b
            if b % a == 0:
                return a

            c= 1
            for i in range(1,max(abs(a),abs(b))):
                if a %i ==0 and  b%i == 0 and i>c:
                    c=i
            return c



        while nxt:
            gdf = ListNode(gcd(cur.val,nxt.val)) 
            cur.next = gdf
            gdf.next = nxt
            cur = nxt
            nxt = nxt.next            


        return head
