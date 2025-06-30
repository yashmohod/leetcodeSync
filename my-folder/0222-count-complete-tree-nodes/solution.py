# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def ca(cur):
            if cur == None:
                return 0
            
            l = ca(cur.left) if cur.left else 0
            r = ca(cur.right) if cur.right else 0

            return l+r+1
        
        return ca(root)
        
