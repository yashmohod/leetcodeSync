class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        lp=candies[0]
        
        for i in candies:
            lp = max(lp,i)
        
        res = []
        for i in candies:
            if i + extraCandies >= lp:
                res.append(True)
            else:
                res.append(False)
        
        return res

