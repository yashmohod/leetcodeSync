class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mp = 0 

        for i in range(len(prices)):
            j = i+1
            while j < len(prices):
                mp = max(prices[j]-prices[i],mp)
                j+=1
        return mp
