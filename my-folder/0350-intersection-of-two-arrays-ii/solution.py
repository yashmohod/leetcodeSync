class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        if len(nums1) > len(nums2):
            for i in nums1:
                if i in nums2 :
                    nums2.remove(i)
                    ans.append(i)
        else:
            for i in nums2:
                if i in nums1 :
                    nums1.remove(i)
                    ans.append(i)
        
        return ans
