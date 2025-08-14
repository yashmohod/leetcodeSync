# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(cur):
            
            l,r = [],[]

            if cur.left != None:
                l = dfs(cur.left)
                for i in range(len(l)):
                    l[i] =str(cur.val)+"->"+l[i]

            if cur.right != None:
                r = dfs(cur.right)
                for i in range(len(r)):
                    r[i] =str(cur.val)+"->"+r[i]

            if cur.left == None and cur.right == None:
                return [str(cur.val)]
            else:
                return l+r
            
        return dfs(root)
