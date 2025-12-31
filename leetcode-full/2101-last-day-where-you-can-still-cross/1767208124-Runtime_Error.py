from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        TOP = n
        BOT = n + 1
        dsu = DSU(n + 2)

        land = [False] * n  # start all water
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def idx(r: int, c: int) -> int:
            return r * col + c

        # add land back from last day to first
        for k in range(n - 1, -1, -1):
            r, c = cells[k]
            r -= 1
            c -= 1
            i = idx(r, c)
            land[i] = True

            if r == 0:
                dsu.union(i, TOP)
            if r == row - 1:
                dsu.union(i, BOT)

            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if 0 <= rr < row and 0 <= cc < col:
                    j = idx(rr, cc)
                    if land[j]:
                        dsu.union(i, j)

            if dsu.find(TOP) == dsu.find(BOT):
                return k  # k is exactly the "last day you can still cross"

        return 0

