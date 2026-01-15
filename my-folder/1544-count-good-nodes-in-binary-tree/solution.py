# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(cur,maxT):

            if root is None:
                return 0
            else:
                res = 0
                res += helper(cur.left,max(maxT,cur.val)) if cur.left else 0
                res += helper(cur.right,max(maxT,cur.val)) if cur.right else 0 
                res += 1 if cur.val >= maxT else 0
                return res
        
        return helper(root,-10**5)

        
