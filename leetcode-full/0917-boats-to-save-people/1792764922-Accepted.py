class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        res = 0
        people.sort()
        N= len(people)
        l,r = 0,N-1

        while l<=r:

            s = people[l] + people[r]

            if s > limit:
                res+=1
                r-=1
            else:
                l+=1
                r-=1
                res+=1
        return res
