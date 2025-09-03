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
        q.append((root,1))

        while q:
            cur,idx = q.popleft()
            if len(res) <= idx:
                res.append([])

            if cur.left != None:
                res[idx].append(cur.left.val)
                q.append((cur.left,idx+1))
            if cur.right != None:
                res[idx].append(cur.right.val)
                q.append((cur.right,idx+1))

        while [] in res:
            res.remove([])
        res.reverse()
        return res
                
            

