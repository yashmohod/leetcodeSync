class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        res = 0 
        s = 0 

        for i in people:

            if s+i > limit:
                res+=1
                s=i
            else:
                s+=i
        
        res+=1 

        return res

