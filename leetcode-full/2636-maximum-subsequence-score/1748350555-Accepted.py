class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        nums = list([x,y] for x,y in zip(nums2,nums1))
        nums.sort(reverse=True)

        heap = []
        summ = 0
        prod = -float("inf")
        
        for i in nums:
            summ += i[1]
            n = i[0]
            heapq.heappush(heap,i[1])
            if k < len(heap):
                summ -= heapq.heappop(heap)
            if k == len(heap):
                prod = max(prod,summ* n )

        return prod
