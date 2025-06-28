class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        s = {}

        for i in nums:
            if i in s:
                s[i] += 1
            else:
                s[i] =1
        
        for i in s.values():
            if i > 1 :
                return False
        
        return True 
