class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def bs(left): 
            l,r=0,len(nums)-1
            i=-1
            while l<=r:
                m = (l+r)//2
                if target > nums[m]:
                    l = m+1
                elif target < nums[m]:
                    r = m-1
                else:
                    i=m
                    if left:
                        r = m-1
                    else:
                        l = m+1
            return i
                    
        l = bs(True)
        r = bs(False)
        return [l,r]
