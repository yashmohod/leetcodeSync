class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mp = float('inf') 
        pr = 0

        for i in prices:
            mp = min(mp,i)
            pr = max(i-mp,pr)
        return pr
        
