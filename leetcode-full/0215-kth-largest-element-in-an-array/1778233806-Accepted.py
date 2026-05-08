class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hh = []
        for i in nums:
            heappush(hh,-i)
        while True:
            c = heappop(hh)
            if k == 1:
                return -c
            k-=1

