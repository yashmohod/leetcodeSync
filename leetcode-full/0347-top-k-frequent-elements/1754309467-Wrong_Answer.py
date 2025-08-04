class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hs = {}
        ans =[]
        for i in nums:
            hs[i] = 1 if i not in hs else hs[i] +1
            if hs[i] == k:
                ans.append(i)
        
        return ans

