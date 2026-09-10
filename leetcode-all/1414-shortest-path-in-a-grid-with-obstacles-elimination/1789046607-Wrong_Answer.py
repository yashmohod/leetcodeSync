class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        q = deque([(0,0,k,0)])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            r,c,d,s = q.popleft()

            if r == len(grid)-1 and c == len(grid[0])-1:
                return s
            
            for dr,dc in dirs:
                rr = r+dr
                cc = c+dc
                if 0<=rr<len(grid) and 0<=cc<len(grid[0]) and grid[rr][cc] == 0:
                    q.append((rr,cc,d,s+1))
                elif 0<=rr<len(grid) and 0<=cc<len(grid[0]) and grid[rr][cc] == 1 and s >0 :
                    q.append((rr,cc,d-1,s+1))

        return -1  
            
