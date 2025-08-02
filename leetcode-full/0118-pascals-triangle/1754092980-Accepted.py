class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []

        for i in range(numRows):
            num=[1]
            if i >0:
                for j in range(len(res[-1])-1):
                    num.append(res[-1][j] + res[-1][j+1])
                num.append(1)
            res.append(num)
        return res
