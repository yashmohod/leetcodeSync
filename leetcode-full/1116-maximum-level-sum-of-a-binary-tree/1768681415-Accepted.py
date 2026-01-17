# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res =[] 
        q = deque([root])
        while q:
            som = 0
            for i in range(len(q)):
                cur = q.popleft()
                if cur is None:
                    continue
                if cur.left:
                    q.append(cur.left) 
                if cur.right:
                    q.append(cur.right)

                som += cur.val
            res.append(som)
        
        m = max(res)
        idx = res.index(m)
        
        return idx+1
                
       
