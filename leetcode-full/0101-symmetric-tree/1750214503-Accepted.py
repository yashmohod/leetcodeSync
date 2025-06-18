# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        l = deque([root.left])
        r = deque([root.right])

        while l and r:
            cl = l.popleft()
            cr = r.popleft()
            if (cr != None and cl == None) or (cr == None and cl != None) :
                return False 
            if (cr != None and cl != None):

                if cr.val != cl.val:
                    return False 

                l.append(cl.left)
                r.append(cr.right)
            
                l.append(cl.right)
                r.append(cr.left)

        if l.count(1) == 0 and r.count(1) == 0:
            return True
        return False           
                

