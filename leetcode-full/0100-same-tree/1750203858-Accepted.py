# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        l = deque([p])
        r = deque([q])

        while l and r:
            cl = l.popleft()
            cr = r.popleft()
            if (cr != None and cl == None) or (cr == None and cl != None) :
                return False 
            if (cr != None and cl != None):

                if cr.val != cl.val:
                    return False 

                l.append(cl.left)
                r.append(cr.left)
            
                l.append(cl.right)
                r.append(cr.right)

        if l.count(1) == 0 and r.count(1) == 0:
            return True
        return False           

