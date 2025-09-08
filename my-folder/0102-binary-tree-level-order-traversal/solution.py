# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None :
            return []
        res = []

        q = deque([])
        q.append((root,0))

        while q:
            cur , idx = q.popleft()
            if len(res)-1 < idx:
                res.append([])
            res[idx].append(cur.val)
            if cur.left != None:
                q.append((cur.left,idx+1))
            if cur.right != None:
                q.append((cur.right,idx+1))
        
        return res

