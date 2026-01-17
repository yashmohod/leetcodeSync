# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = [] 
        def dfs(cur,d):
            if cur is None:
                return
            else:
                if len(self.res) == d:
                    self.res.append(cur.val)
                
                dfs(cur.right,d+1)
                dfs(cur.left,d+1)
        dfs(root,0) 
        return self.res

        

                    




