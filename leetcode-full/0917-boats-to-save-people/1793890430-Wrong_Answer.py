class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
      
        
        f = Counter(people)
        res = 0 
        for i in people:
            if f[i] <=0:
                continue            
            d = limit - i

            if d in f and f[d]>0:
                f[d] -=1
            f[i] -=1
            res+=1
        
        
        return res

      
