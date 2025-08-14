class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(row,target):
            left=0
            right=len(row)-1
            while left<=right:
                mid=(left+right)//2
                if row[mid]==target:
                    return True
                elif row[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            
    
        for row in matrix:
            if row[0]<=target<=row[-1]:
                if binary_search(row,target):
                    return True
        return False
