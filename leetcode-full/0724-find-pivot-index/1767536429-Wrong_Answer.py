class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        l = [0]*len(nums)
        r = [0]*len(nums)
        res = len(nums)
        for i in range(1,len(nums)):
           l[i] = nums[i-1] + l[i-1] 
       
        for i in range(len(nums)-2, -1, -1):
            r[i] = nums[i+1] + r[i+1]
            if r[i] == l[i]:
                res = min(res,i) 


            
        return -1 if res == len(nums) else res



        
