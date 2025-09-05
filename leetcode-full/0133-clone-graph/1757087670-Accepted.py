"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        
        if node == None:
            return node
        made = {}
        res = Node(1,[])
        made[res.val] = res
        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n.val not in made:
                    n_cur = Node(n.val,[made[cur.val]])
                    made[n.val] = n_cur
                    made[cur.val].neighbors.append(n_cur)
                    q.append(n)
                else:
                    if made[cur.val] not in made[n.val].neighbors:
                        made[n.val].neighbors.append(made[cur.val])
                    
        # for x,y in made.items():
        #     print(x,y)
        return res



        
        


