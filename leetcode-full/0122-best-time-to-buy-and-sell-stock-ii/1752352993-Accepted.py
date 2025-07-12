class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        for i in range(len(prices)):

            if i +1 < len(prices):
                prices[i] = prices[i+1] - prices[i] 
            else:
                prices[i] = 0 
        
        sum = 0 

        for i in prices:
            if i > 0 :
                sum += i 
        
        return sum 
