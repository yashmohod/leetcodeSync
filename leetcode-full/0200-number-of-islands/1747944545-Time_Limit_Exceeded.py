class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0

        islands = 0 
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs (r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                r,c = q.popleft()
                visited.add((r,c))
                for dr,dc in directions:
                    rn = dr +r
                    cn = dc +c
                    if(
                        (rn,cn) not in visited and
                        rn in range(rows)and 
                        cn in range(cols)and
                        grid[rn][cn] == "1"
                    ):
                        q.append((rn,cn))



        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands

