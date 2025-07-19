from sortedcontainers import SortedList
from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        s1 = SortedList()
        ans = float('inf')
        
        for i in range(1, n + 1):
            if i >= l:
                s1.add(prefix[i - l])
            if i > r:
                s1.remove(prefix[i - r - 1])
            
            idx = s1.bisect_left(prefix[i])
            if idx > 0:
                best_prefix = s1[idx - 1]
                sub_sum = prefix[i] - best_prefix
                if sub_sum > 0:
                    ans = min(ans, sub_sum)
        
        return ans if ans != float('inf') else -1
