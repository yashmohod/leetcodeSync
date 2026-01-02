class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        
        ave = 0
        res = 0
        for i in range(len(nums)):
            if i < k :
                ave += nums[i]
                res =  ave
            else:
                ave += nums[i] -nums[i- k]
                res = max(ave,res)

        return res/k
