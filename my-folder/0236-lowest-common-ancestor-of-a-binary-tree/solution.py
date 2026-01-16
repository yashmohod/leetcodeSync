# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(cur):
            if cur is None:
                return None
            else:

                if cur == p or cur == q:
                    return cur

                l = dfs(cur.left) if cur.left else None
                r = dfs(cur.right) if cur.right else None

                if l != None and r != None:
                    return cur
                elif l is None:
                    return r
                elif r is None:
                    return l 
                else:
                    return None

        return dfs(root)
