class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        v = []

        def bt(r):
            if r not in v :
                v.append(r)
            
            for i in r:
                t = r.copy()
                t.remove(i)
                bt(t)
        
        bt(nums)

        return v
