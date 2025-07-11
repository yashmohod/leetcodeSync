class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        k = k % len(nums)
        ans = [0]*len(nums)

        for i in range(len(nums) - k ):
            ans[i+k] = nums[i]
        
        for i in range(k):
            ans[k-1-i] = nums[-(i+1)]
        for i in range(len(nums)):
            nums[i] = ans[i]


        
