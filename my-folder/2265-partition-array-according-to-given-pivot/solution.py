class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        small = []
        big = []
        equal = []
        count = 0

        for n in nums:
            if n < pivot:
                small.append(n)
            elif n > pivot:
                big.append(n)
            else:
                equal.append(n)
        
        ans = small + equal + big

        return ans
