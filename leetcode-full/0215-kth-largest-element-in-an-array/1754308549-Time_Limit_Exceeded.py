class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        def qs(l,r):

            piv,p = nums[r],l

            for i in range(l,r):
                if nums[i] < piv:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            
            nums[p], nums[r] = nums[r], nums[p]

            if k > p:
                return qs(p+1,r)
            elif k < p:
                return qs(l,p-1)
            else:
                return nums[p]

        return qs(0,len(nums)-1)



