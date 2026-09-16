class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        
        rows, cols = len(mat), len(mat[0])
        res = [[-1]*cols for _ in range(rows)]
        q = deque()

        for y in range(rows):
            for x in range(cols):
                if mat[y][x] == 0:
                    res[y][x] = 0
                    q.append((x, y))

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                xx, yy = x+dx, y+dy
                if 0 <= xx < cols and 0 <= yy < rows and res[yy][xx] == -1:
                    res[yy][xx] = res[y][x] + 1
                    q.append((xx, yy))
        return res
                        

                        


