# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None :
            return False
        def has(cur,prevVal,target):

            if cur.left  == None and cur.right == None :
                if prevVal+cur.val == target :
                    return True 
                else:
                    return False
            else:
                l,r = False,False
                if cur.left != None:
                    l = has(cur.left,prevVal+cur.val,target)
                if cur.right != None:
                    r = has(cur.right,prevVal+cur.val,target)

                return l or r 

        return has(root,0,targetSum)
            
            

