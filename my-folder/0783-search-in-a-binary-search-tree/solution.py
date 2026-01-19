# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            return None
        else:
            if root.val == val :
                return root
            r = None
            if val > root.val:
                r = self.searchBST(root.right,val) if root.right != None else None
            elif val < root.val:
                r = self.searchBST(root.left,val) if root.left != None else None
            return r
            
