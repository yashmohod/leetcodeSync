class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        d = {}

        for i in nums:
            d[i] = d.get(i,0)+1

        res = 0

        for i in nums:
            diff = k - i
            print(i,diff, d[i],d[diff] if diff in d else -1)
            if diff in d and d[diff] > 0 and d[i] >0:
                if i == diff and d[i] < 2:
                    continue
                res += 1
                d[i] = d[i] -1
                d[diff] = d[diff] -1

        return res
