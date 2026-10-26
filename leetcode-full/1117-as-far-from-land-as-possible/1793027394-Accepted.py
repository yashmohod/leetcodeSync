class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
      
        q=deque([])
        z,o = 0,0
        N=len(grid)
        for y in range(N):
            for x in range(N):
                if grid[y][x] == 1 :
                    o+=1
                    q.append((x,y))
                else:
                    z+=1
        if z == N*N or o ==N*N:
            return -1
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        res = 0 
        count = 1
        while q:
            c = len(q)
            while c > 0 : 
                x,y = q.popleft()
                for dx,dy  in dirs:
                    xx,yy = x+dx, y+dy
                    if 0<=xx<N and 0<=yy<N and grid[yy][xx] ==0:
                        grid[yy][xx] = count
                        res = max(res,count) 
                        q.append((xx,yy))
                c-=1 
            count+=1
        return res
