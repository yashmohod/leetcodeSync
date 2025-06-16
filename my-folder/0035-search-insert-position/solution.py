class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r = len(nums)-1
        cur = 0 
        while l<=r:
            cur = (r+l)//2

            if nums[cur] == target:
                return cur

            if nums[cur] > target:
                r = cur -1
            else:
                l = cur +1
        
        return l 


