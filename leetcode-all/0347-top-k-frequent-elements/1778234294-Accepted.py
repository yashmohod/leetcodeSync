class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for i in nums:
            f[i] = f.get(i,0)+1
        rp = []
        for x,y in f.items():
            rp.append([y,x])
        rp.sort(reverse=True)
        
        res = []
        for y,x in rp:
            res.append(x)
            if len(res)>=k:
                break
        return res
