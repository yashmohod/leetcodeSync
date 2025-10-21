import numpy as np 
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        lp = max(candies)
        res =  (np.array(candies) +extraCandies) >= lp
        res = res.tolist()
        return res
