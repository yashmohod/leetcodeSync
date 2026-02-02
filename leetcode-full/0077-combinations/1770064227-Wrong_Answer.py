class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        res = []
        for i in range(1,n):
            j = i +1
            while j <=n:
                res.append([i,j])
                j+=1
        
        return res
