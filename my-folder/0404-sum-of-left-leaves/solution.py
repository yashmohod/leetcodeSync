# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def pu(cur,l):

            if cur.left == None and cur.right == None:
                if l:
                    return cur.val
                else:
                    return 0 

            l,r = 0,0
            if cur.left != None:
                l = pu(cur.left,True)
            if cur.right != None:
                r = pu(cur.right,False)
            
            return l+r 
        
        return pu(root,False)

            

            

