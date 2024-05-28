class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start=0
        end=k
        sum=0
        for i in nums[start:end]:
                sum+=i
        la = sum

        if len(nums) == 1:
            return nums[0]
        while end<len(nums):
            sum = sum - float(nums[start])
            sum = sum + float(nums[end]) 
            la = max(la, sum)
            start+=1
            end+=1
        return la/k
