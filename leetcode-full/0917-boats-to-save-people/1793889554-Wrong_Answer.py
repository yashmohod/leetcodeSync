class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
      
        people.sort()

        res = 0 
        s = 0 
        for i in people:
            if s+i> limit:
                res+=1
                s=i
            elif s+i < limit:
                s+=i
            else:
                res+=1
                s=0
        return res+1 if s>0 else res
    

      
