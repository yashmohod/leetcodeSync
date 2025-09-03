# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        res = [[root.val]]

        q = deque()
        q.append(root)

        while q:
            cur = q.popleft()
            ca = []
            if cur.left != None:
                ca.append(cur.left.val)
                q.append(cur.left)
            if cur.right != None:
                ca.append(cur.right.val)
                q.append(cur.right)
            if len(ca)>0:
                res.append(ca)

        res.reverse()
        return res
                
            

