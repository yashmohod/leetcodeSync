# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0 

        def dfs(cur,dis,left):
            if cur != None :
                self.res = max(self.res,dis)
                if left:
                    dfs(cur.right,dis+1,False)
                    dfs(cur.left,1,True)
                else:
                    dfs(cur.right,1,False)
                    dfs(cur.left,dis+1,True)
        
        dfs(root,0,True)
        dfs(root,0,False)

        return self.res




