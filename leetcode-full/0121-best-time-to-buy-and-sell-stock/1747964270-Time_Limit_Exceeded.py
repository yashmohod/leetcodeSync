class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        curMax = 0
        for i in range(n):
            for j in range(i+1,n):
                curMax = max(curMax,prices[j] - prices[i])
    
        return curMax
        
