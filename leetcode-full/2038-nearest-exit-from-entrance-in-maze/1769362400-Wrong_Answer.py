class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        low = float('inf')
        q = deque([])
        seen=set()
        ys,xs = entrance
        q.append((xs,ys,-1))
        seen.add((xs,ys))
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        found = False
        while q:
            x,y,d = q.popleft()
            if x!=xs and y!=ys and x in [0,len(maze[0])-1]  and y in [0,len(maze)]:
                low = min(low,d)
                found = True
            for dx,dy in dirs:
                xx = x+dx
                yy = y+dy
                if xx in range(len(maze[0])) and yy in range(len(maze)) and (xx,yy) not in seen:
                    seen.add((xx,yy))
                    q.append((xx,yy,d+1))
        print(found)
        return low if found else -1

