class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0,1,1]
        if n < 3 :
            return sum(nums[:n])

        for i in range(n-2):
            print(nums)
            nums.append(sum(nums))
            nums = nums[1:]

        return nums[-1]
