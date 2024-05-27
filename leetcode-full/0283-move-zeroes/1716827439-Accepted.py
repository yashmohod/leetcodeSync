class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numslen=len(nums)
        count=0
        for i in range(numslen):
            if nums[i] !=0:
                nums.append(nums[i])
            else:
                count+=1
        for i in range(numslen):
            nums.pop(0)
        for i in range(count):
            nums.append(0)
