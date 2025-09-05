# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(cur,sumTill):

            if cur.left == None and cur.right == None:
                if cur.val +sumTill == targetSum:
                    return [[cur.val]]
            l= []
            r= []
            if cur.left != None:
                l = dfs(cur.left,sumTill + cur.val)
            if cur.right != None:
                r = dfs(cur.right,sumTill + cur.val)
            
            for i in range(len(l)):
                l[i].append(cur.val)
            
            for i in range(len(r)):
                r[i].append(cur.val)
            
            return l+r
        
        res = dfs(root,0)

        for i in range(len(res)):
            res[i].reverse()
        return res

