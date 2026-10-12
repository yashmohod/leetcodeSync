class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        p = {}
        s = 0 
        r = 0 

        for i in nums:
            p[s] = p.get(s,0)+1
            s+=i
            d = s-k
            if d in p :
                r +=p[d]
        return r

                
       
       
        
            
        
        

            
