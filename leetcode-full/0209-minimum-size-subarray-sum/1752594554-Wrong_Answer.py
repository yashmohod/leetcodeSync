class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        ssf = 0 
        hp={}
        count = float('inf')
        for i,num in enumerate(nums):
            ssf+=num
            if target- num == 0:
                return 1
            # print(i,ssf)
            if ssf - target in hp:
                count = min(count,i-hp[ssf - target])

            hp[ssf] = i

        if ssf < target or count == float('inf') :
            return 0
        else:
            return count
