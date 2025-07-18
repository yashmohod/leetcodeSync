class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        r,c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(1,c):
                matrix[i][j] += matrix[i][j-1]
                
        for i in range(1,r):
            for j in range(c):
                matrix[i][j] += matrix[i-1][j]

        
        return k

        


        
