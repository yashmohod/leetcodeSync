class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profitsForEach = []

        for i in range(n):
            curDayProfit =[]
            for j in range(i+1,n):
                curDayProfit.append(prices[j] - prices[i])
            profitsForEach.append(curDayProfit)
        curMax = 0
        for i in profitsForEach:
            if len(i) !=0:
                curMax = max(curMax,max(i))

        return curMax
        
