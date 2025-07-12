class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        for i in range(len(prices)):

            if i +1 < len(prices):
                if prices[i+1] - prices[i] > 0 :
                    sum += prices[i+1] - prices[i] 

    
        return sum 
