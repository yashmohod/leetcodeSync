class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        l,r = 0,len(matrix[0]) -1

        while l<r:

            m = (l+r) //2

            if matrix[0][m] == target:
                return True
            if matrix[0][m] < target:
                l = m +1
            elif matrix[0][m] > target:
                r = m -1
        
        ll,rr = 0,len(matrix[0][:]) -1

        while ll<rr:

            m = (ll+rr) //2

            if matrix[l][m] == target:
                return True
            if matrix[l][m] < target:
                ll = m +1
            elif matrix[l][m] > target:
                rr = m 
        
        return False
