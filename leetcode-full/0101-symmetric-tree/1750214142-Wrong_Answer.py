# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root == None or (root.left != None and root.right == None) or (root.left == None and root.right != None) :
            print("1")
            return False
        
        l = deque([root.left])
        r = deque([root.right])

        while l and r:
            cl = l.popleft()
            cr = r.popleft()
            if (cr != None and cl == None) or (cr == None and cl != None) :
                print("2")
                return True 
            if (cr != None and cl != None):

                if cr.val != cl.val:
                    print("2")
                    return True 

                l.append(cl.left)
                r.append(cr.left)
            
                l.append(cl.right)
                r.append(cr.right)

        if l.count(1) == 0 and r.count(1) == 0:
            print("3")
            return False
        print("4")
        return True 
                

