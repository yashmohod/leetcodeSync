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
                ml,mr=m-1,m
                while ml-1 <0 and nums[ml-1] ==target:
                    ml-=1
                while mr+1 < len(nums) and nums[mr+1] ==target:
                    mr+=1
                return [ml,mr]

        return [-1,-1]
