class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        fr = {}

        for i in nums:
            fr[i] = 1 if i not in fr else fr[i] +1
        
        res = []
        for x, y in fr.items():
            res.append([y,x])
        res.sort(reverse=True)

        ans = []
        for i in range(k):
            ans.append(res[i][1])
        return ans

