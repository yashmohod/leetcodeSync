class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        ss=[]

        for i in nums:
            if i in ss:
                return True
            ss.append(i)

        return False

