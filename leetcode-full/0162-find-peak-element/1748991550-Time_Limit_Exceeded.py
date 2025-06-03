class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l = 0 
        r = len(nums) - 1 
        m = round((r+l)/2) 
        if len(nums) == 1:
            return 0

        while True:
            
            if m == 0 and  nums[m] > nums[m+1]:
                break
            elif m == len(nums) - 1 and  nums[m] > nums[m-1]:
                break
            elif nums[m] > nums[m-1] and  nums[m] > nums[m+1]:
                break
            

            if nums[m] < nums[m-1]:
                r = m
            if nums[m] < nums[m+1]:
                l = m+1
            m = round((r+l)/2) 

        return m


        

            
