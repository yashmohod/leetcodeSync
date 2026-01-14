# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getSeq(root):
            
            if root.left is None and root.right is None:
                return [str(root.val)]
            else:
                l = getSeq(root.left) if root.left else []
                r = getSeq(root.right) if root.right else []
                return l+r

        r1 = getSeq(root1) 
        r2 = getSeq(root2)
        return r1 == r2
        
