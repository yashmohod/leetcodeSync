class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)

        res1 = a - a.intersection(b)
        res2 = b - b.intersection(a)

        return [list(res1),list(res2)]
