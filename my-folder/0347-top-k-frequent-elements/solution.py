class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buc = [[] for _ in range(len(nums)+1)]
        h = {}
        for i in nums:
            h[i] = h.get(i,0)+1
        for i,x in h.items():
            buc[x].append(i)

        res = []
        c = len(nums)-1
        while len(res)<k:
            if buc[c]:
                res.append(buc[c].pop())
            else:
                c-=1
        return res
        
