class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        l,r=0,1
        while r < len(nums) and nums[r-1] < nums[r]:
            r+=1
        
        l=r - len(nums)
        r = r-1
        print(l,r)
        while l<=r:
            m = (l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m if m >= 0 else len(nums)+m
        return -1 

