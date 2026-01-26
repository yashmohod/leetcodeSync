class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:


        nums = [[x,y] for x,y in zip(nums2,nums1)]
        nums.sort(reverse=True)
        print(nums)
        score = 0 
        minh = []
        s = 0
        for n2,n1 in nums:
            s +=n1
            heapq.heappush(minh,n1)
            print(minh,s,n1,n2)
            if len(minh) == k:
                score = max(s*n2,score)
                s -= heapq.heappop(minh)
           
            

        return score

