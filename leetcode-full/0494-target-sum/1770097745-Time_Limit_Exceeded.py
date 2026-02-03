class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cur =[]
        def bt(i):
            if i == len(nums):
                return 1 if sum(cur) == target else 0
            c = 0
            cur.append(-int(nums[i]))
            c+=bt(i+1)
            cur.pop()

            cur.append(int(nums[i]))
            c+=bt(i+1)
            cur.pop()
            return c
        
        return bt(0)
