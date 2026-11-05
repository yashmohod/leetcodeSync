class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        people.sort()
        res = 0 
        l,r = 0,len(people)-1

        while l<=r:

            s = people[l] + people[r]

            if s <= limit:
                res+=1
                l+=1
                r-=1
            else:
                res+=1
                r-=1

        return res

      
