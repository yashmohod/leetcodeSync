class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        r = []

        for i in range(numRows):
            if i == 0:
                r.append([1])
            elif i == 1:
                r.append([1,1])
            else:
                a = [1]
                for j in range(len(r[-1])-1):
                    a.append(r[-1][j]+r[-1][j+1])
                a.append(1)
                r.append(a)
        return r
