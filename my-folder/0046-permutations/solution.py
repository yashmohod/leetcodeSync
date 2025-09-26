class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        res = [] 

        def bt(r,t):
            if len(r) >0 :

                for i in r:
                    cr = r.copy()
                    cr.remove(i)
                    bt(cr,t+[i])
            else:
                res.append(t)
        bt(nums,[])
        print(res)

        return res
