class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        res = 0
        alt = 0
        for i in gain:

            alt += i 
            res = max(alt,res)

        return res
