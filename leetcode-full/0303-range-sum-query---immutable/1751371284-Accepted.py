class NumArray:

    def __init__(self, nums: List[int]):
        self.ar = nums
        

    def sumRange(self, left: int, right: int) -> int:
            su = 0 
            for i in range(left,right+1):
                su += self.ar[i]
            return su

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
