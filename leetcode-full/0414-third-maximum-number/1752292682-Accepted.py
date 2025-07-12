class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        maxes = []
        for i in nums:
            if not(i in maxes):
                maxes.append(i)
        
        maxes.sort()
        maxes.reverse()
        if len(maxes)< 3:
            return maxes[0]
        else:
            return maxes[2]
