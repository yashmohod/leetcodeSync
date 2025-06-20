# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

   
        def helper(cur):
            if cur == None:
                return 0, True

            l,ll = helper(cur.left)
            r,rr = helper(cur.right)

            return max(l,r)+1, (ll and rr) and (abs(l-r)<=1)
            
        ere,found = helper(root)

        return found

