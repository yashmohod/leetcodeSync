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
        if not node:
            return node
        d = {}
        visited = set()
        q = deque([node])
        visited.add(node.val)
        while q: 
            cur = q.pop()

            if cur.val not in d:
                d[cur.val] = Node(cur.val)
            
            for neighbor in cur.neighbors:
                if neighbor.val not in visited:
                    q.append(neighbor)
                if neighbor.val not in d:
                    d[neighbor.val] = Node(neighbor.val)
                
                d[cur.val].neighbors.append(d[neighbor.val])
                visited.add(neighbor.val)
        
        return d[node.val]
