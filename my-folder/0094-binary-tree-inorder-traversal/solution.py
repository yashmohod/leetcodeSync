# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        def bst(rr): 
            if rr.left == None and rr.right == None:
                return [rr.val]
            l=[]
            r=[]
            if rr.left != None:
                l = bst(rr.left)
            if rr.right != None:
                r = bst(rr.right) 
            return l+[rr.val]+r

        return bst(root)
