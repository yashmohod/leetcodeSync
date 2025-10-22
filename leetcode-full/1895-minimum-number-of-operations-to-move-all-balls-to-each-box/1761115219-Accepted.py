class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        b = list(boxes)
        res = [0]*n
        for i in range(n):
            m = 0 
            for j in range(n):
                if j != i and b[j] == "1":
                    m+= abs(i-j)
            res[i] =m
        return res


