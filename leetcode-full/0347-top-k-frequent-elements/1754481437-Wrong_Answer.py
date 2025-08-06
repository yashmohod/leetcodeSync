class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        fr = {}

        for i in nums:
            fr[i] = 1 if i not in fr else fr[i] +1
        
        res = []
        for x, y in fr.items():
            res.append([x,y])
        res.sort()

        print(res)

