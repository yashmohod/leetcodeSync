class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

       
        mat = [[0 for _ in range(col)] for _ in range(row)]
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(len(cells)):
            mat[cells[i][0]-1][cells[i][1]-1] = 1
            stack = [(0,j) for j in range(col)]
            found = False
            seen = set()
            while len(stack) > 0:
                x,y = stack.pop()
                seen.add((x,y))
                if x == row -1:
                    found = True
                    break
                if mat[x][y] == 0:
                    for dx,dy in dirs:
                        xx = x+dx
                        yy = y+dy 
                        if xx in range(row) and yy in range(col) and (xx,yy) not in seen and mat[xx][yy] == 0:
                            stack.append((xx,yy))
            if not found:
                return i 
            


