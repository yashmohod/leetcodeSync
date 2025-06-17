class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        t = nums1 + nums2
        t.sort()
        print(t)
        t = t[n:]
        print(nums1)
        for i in range(len(nums1)):
            nums1[i] = t[i]
