# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        


        def dfs(cur):
            if cur == None:
                return 0,0
            
            lm,nsl = dfs(cur.left)
            rm,nsr = dfs(cur.right)
            m = max(lm,rm)
            ns = max(nsl,nsr)
            return m+cur.val,max(lm+rm+cur.val,ns)
        
        l,r = dfs(root)

        return max(l,r)

