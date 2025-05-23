class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        temp = prices.copy() 
        temp.sort()
        temp2 = temp.copy().reverse()

        # print(prices)
        # print(temp)
        # print(prices == temp)
        # print(prices == temp2)
        if prices == temp:
            return temp[-1] - temp[0]
        if prices == temp2:
            return 0
        curMax = 0
        for i in range(n):
            for j in range(i+1,n):
                curMax = max(curMax,prices[j] - prices[i])
    
        return curMax
        
