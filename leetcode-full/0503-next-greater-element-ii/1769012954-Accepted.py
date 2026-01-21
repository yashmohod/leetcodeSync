class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        st = []  # stack of indices

        for i in range(2 * n):
            idx = i % n

            while st and nums[st[-1]] < nums[idx]:
                res[st.pop()] = nums[idx]

            # only push indices in the first pass
            if i < n:
                st.append(idx)

        return res

