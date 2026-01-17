# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []

        q = deque([root])

        while q :
            t = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur is None:
                    continue
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)  
                t.append(cur.val)
            res.append(t)
        
        return res

            
