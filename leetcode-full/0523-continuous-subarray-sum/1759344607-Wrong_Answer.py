class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    
        s ={}
        som = 0
        for i in range(len(nums)):
            som +=nums[i]
            t = som - k 
            # print(som,t,s)
            if t in s:
                return True
            s[som] = i
        return False

