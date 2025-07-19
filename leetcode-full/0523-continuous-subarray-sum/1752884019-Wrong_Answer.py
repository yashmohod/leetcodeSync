class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        r=0

        while r < len(nums):

            if nums[r] % k == 0  :
                return True 
            l = 0 
            while l<r:
                print((nums[r] - nums[l]) % k)
                if (nums[r] - nums[l]) % k == 0 :
                    return True 
                l +=1
            r +=1
        
        return False
