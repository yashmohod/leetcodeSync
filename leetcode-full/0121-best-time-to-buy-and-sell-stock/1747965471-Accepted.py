class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_ = float('inf')
        maxPrf =0
        for i in prices:
            min_ = min(i,min_)
            maxPrf = max(maxPrf,i- min_)
    
        return maxPrf
        
