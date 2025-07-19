class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        top = -float('inf')
        som = 0 
        for i in range(len(nums)):

            som += nums[i]/k
            # print(i,som)
            if i >= k - 1:
                top = som if som > top else top
                som -=nums[i-k]/k
                print(i,som,nums[i-k])
        
        return top 
            


