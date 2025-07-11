class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def rotate():
            last = nums[-1]
            count = 0 
            while count < len(nums):
                nums[count],nums[0] = nums[0],nums[count]
                count+=1
            nums[0] = last
        
        for i in range(k):
            rotate()


        
