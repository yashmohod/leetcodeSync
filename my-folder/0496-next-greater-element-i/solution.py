class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ind = {}
        for i in range(len(nums1)):
            ind[nums1[i]] = i

        res = [-1]*len(nums1)
        s = []
        for i in nums2:
            while s and i> s[-1]:
                c = s.pop()
                res[ind[c]] = i
            if i in ind:
                s.append(i)

       
            
        return res
