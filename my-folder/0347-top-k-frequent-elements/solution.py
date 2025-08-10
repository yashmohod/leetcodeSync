class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        fr = {}

        for i in nums:
            fr[i] = 1 if i not in fr else fr[i] +1 
        
        buc =  [[] for _ in range(len(nums) + 1)]

        for key,val in fr.items():
            buc[val].append(key)
        
        res = []
        for i in range(len(buc)):
            if buc[len(buc)-1-i]:
                for j in  buc[len(buc)-1-i]:
                    if k > 0:
                        res.append(j)
                        k -=1
                    else:
                        break

        return res

