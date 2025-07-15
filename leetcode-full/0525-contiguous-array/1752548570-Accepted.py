class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = 0 

        res = 0 
        di = {}
        for i,num in enumerate(nums):

            if num == 0 :
                diff -=1
            else:
                diff +=1
            
            if diff not in di:
                di[diff] = i
            
            if diff == 0 :
                res = i +1
            else:
                res = max(res,i - di[diff])
        
        return res
