# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def helper(cur):
            if cur.right == None and cur.left == None:
                return 1
            if cur.right != None and cur.left != None:
                l = helper(cur.left)
                r = helper(cur.right)
                return min(l+1,r+1)
            elif cur.right != None and cur.left == None:
                return helper(cur.right) +1
            elif cur.right == None and cur.left != None:
                return helper(cur.left) +1

        return helper(root)
        
