class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        y = len(matrix)
        x = len(matrix[0])

        for i in range(y):
            for j in range(1,x):
                matrix[i][j] += matrix[i][j-1]
        for i in range(1,y):
            for j in range(x):
                matrix[i][j] += matrix[i-1][j] 
            

        if matrix[-1][-1] == k:
            return k
        else:
            for i in range(y):
                for j in range(x):
                    if matrix[i][j] == k:
                        return k
