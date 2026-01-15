# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        

        def countL(cur,st):

            if cur is None:
                return 0
            else:

                st.append(cur.val)
                lc = countL(cur.left,st) if cur.left else 0
                rc = countL(cur.right,st) if cur.right else 0
                st.pop()

                r = cur.val
                res = 0
                for i in range(-1,-len(st)-1,-1):
                    r +=st[i]
                    if r == targetSum:
                        res +=1
      
                return lc+rc+res
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1 if root.val == targetSum else 0
        else:
            return countL(root,deque([])) +1 if root.val == targetSum else countL(root,deque([]))
            
                








