class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        c = {}
        r = 0

        for i in range(len(grid)):
            a = [str(j) for j in grid[i]]
            a = "".join(a)
            b = [ ]
            for j in range(len(grid)):
                b.append(str(grid[j][i]))

            b = "".join(b)
            r += 1 if a in c else 0 
            c[a] = c.get(a,0) +1 
            r += 1 if b in c else 0
            c[b] = c.get(b,0) +1

        return  r

