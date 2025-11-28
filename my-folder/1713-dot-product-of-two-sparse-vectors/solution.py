class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = {}

        for i,x in enumerate(nums):
            if x !=0:
                self.v[i]=x

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        d = 0

        for key,val in vec.v.items():
            d+= self.v.get(key,0)*val
        return d

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
