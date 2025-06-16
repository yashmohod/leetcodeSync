class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r = len(nums)-1
        cur = 0 
        while l<r:
            cur = int((r+l)/2)

            if nums[cur] == target:
                return cur

            if nums[cur] > target:
                r = cur 

            if nums[cur] < target:
                l = cur
        
        return cur 


