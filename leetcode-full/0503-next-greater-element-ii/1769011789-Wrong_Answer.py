class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = []
        kv = {}
        for i in range(n*2):
            idx = i %n
            while st and st[-1] < nums[idx]:
                kv[st.pop()]= nums[idx]
            
            st.append(nums[idx])
        res = []
        for i in nums:
            res.append(kv.get(i,-1))
        return res

