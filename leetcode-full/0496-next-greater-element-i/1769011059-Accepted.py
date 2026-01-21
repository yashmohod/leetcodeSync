class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        st = []
        kv = {}
        for i in nums2:
            while st and st[-1] < i :
               kv[st.pop()] = i 
            st.append(i)
        for i in range(len(nums1)):
            nums1[i] = kv.get(nums1[i] ,-1)
        
        return nums1

