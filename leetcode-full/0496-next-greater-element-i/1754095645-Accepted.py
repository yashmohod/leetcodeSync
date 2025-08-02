class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ind = {}
        for i in range(len(nums2)):
            ind[nums2[i]] = i

        res = []
        for i in nums1:
            g = i 
            c = ind[i]
            while c < len(nums2):
                if g < nums2[c]:
                    g = nums2[c]
                    break
                c +=1
            if g == i :
                res.append(-1)
            else:
                res.append(g)
            
        return res
