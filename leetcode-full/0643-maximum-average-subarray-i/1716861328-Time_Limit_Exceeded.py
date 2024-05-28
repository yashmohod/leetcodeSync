class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start=0
        end=k
        sum=0
        for i in nums[start:end]:
                sum+=i
        la = sum/k
        if len(nums) == 1:
            return nums[0]
        while end<=len(nums):
            sum=0
            for i in nums[start:end]:
                sum+=i
            if sum/k >la:
                la= sum/k
            start+=1
            end+=1
        return la
