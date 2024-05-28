class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        la=0

        for i in range(len(grid)):
            count=-1
            for k in range(len(grid)):
                if Counter(grid[i]) == Counter(grid[k]):
                    count+=1
            for j in range(len(grid[i])):
                if Counter(grid[i]) == Counter(grid[:][j]):
                    count+=1

            la=max(la,count)

        return la
