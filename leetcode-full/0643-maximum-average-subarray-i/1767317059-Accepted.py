class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        
        ave = 0
        for i in range(k):
            ave += nums[i]
        res =  ave
        for i in range(k, len(nums)):
            ave += nums[i] -nums[i- k]
            res = max(ave,res)

        return res/k
