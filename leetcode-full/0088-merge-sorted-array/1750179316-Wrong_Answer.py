class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n ==0:
            return
        r = 0

        for l in range(len(nums1)):
            if l>=m:
                nums1[l] = nums2[r]
                r+=1
            else:
                if nums1[l] >= nums2[r]:
                    nums1[l], nums2[r] =nums2[r], nums1[l]
