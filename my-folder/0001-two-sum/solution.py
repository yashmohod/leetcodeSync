class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        si = {}

        for i,x in enumerate(nums):
            d = target-x
            if d in si:
                return [si[d],i]
            si[x]=i
        return []
