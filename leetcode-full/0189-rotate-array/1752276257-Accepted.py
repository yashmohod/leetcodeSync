class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        k = k % len(nums)
        ans = [0]*len(nums)

        for i in range(len(nums) - k ):
            print(nums[i])
            ans[i+k] = nums[i]
        
        for i in range(k):
            print(nums[-(i+1)],k-1-i)
            ans[k-1-i] = nums[-(i+1)]
        for i in range(len(nums)):
            nums[i] = ans[i]


        
