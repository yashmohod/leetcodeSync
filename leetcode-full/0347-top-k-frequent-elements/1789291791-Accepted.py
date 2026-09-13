class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numk = Counter(nums)
        h = []
        for num,freq in numk.items():
            heapq.heappush(h,(freq,num))
            if len(h)>k:
                heapq.heappop(h)
 
        return [v for j,v in h]
