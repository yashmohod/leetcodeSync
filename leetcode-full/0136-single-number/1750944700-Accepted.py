class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        for i in range(len(nums)-1):

            nums[i+1] = nums[i+1] ^ nums[i]

        return nums[-1]



