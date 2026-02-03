class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zs = 0 

        for i in nums:
            if i:
                p*=i
            else:
                zs+=1
        
        if zs > 1:
            return [0]*len(nums)
        elif zs == 1:
            re = [0]*len(nums)
            re[nums.index(0)] = p
            return re
        else:
            re = []
            for i in nums:
                re.append(p//i)
            return re
