class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def qs(l,r):
            if l>=r:
                return 

            piv,p = nums[r],l

            for i in range(l,r):
                if nums[i] < piv:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            
            nums[p], nums[r] = nums[r], nums[p]

            qs(l,p-1)
            qs(p+1,r)

        qs(0,len(nums)-1)
        return nums[len(nums)-k]


