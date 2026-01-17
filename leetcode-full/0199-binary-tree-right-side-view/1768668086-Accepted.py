# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
             
        res = [[root.val]]

        q = deque([])

        q.append([root,1])
        while q :
            cur,idx = q.popleft()
            
            if idx < len(res):
                if cur.left:
                    res[idx].append(cur.left.val)
                    q.append([cur.left,idx+1])
                if cur.right:
                    res[idx].append(cur.right.val)
                    q.append([cur.right,idx+1])
            else:
                t = []
                if cur.left:
                    t.append(cur.left.val)
                    q.append([cur.left,idx+1])
                if cur.right:
                    t.append(cur.right.val)
                    q.append([cur.right,idx+1])
                res.append(t)
        
        ret = []
        for i in res:
            if len(i)> 0:
                ret.append(i[-1])
        return ret

        

                    




