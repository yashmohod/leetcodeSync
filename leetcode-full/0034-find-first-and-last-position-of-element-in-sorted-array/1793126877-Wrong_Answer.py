class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l,r=0,len(nums)-1
        while l<r:
            m = (l+r)//2

            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
            else:
                return [l,r-1]

        return [-1,-1]
