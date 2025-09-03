# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = [root.val]

        def dfs(cur):
            if cur == None:
                return 0
            
            lm = dfs(cur.left)
            rm = dfs(cur.right)
            lm = max(lm,0)
            rm = max(rm,0)

            res[0] = max(lm+rm+cur.val,res[0])

            return max(lm+cur.val, rm+cur.val)
        
        dfs(root)

        return res[0]

