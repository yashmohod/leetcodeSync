class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       minCost = 0 
       idx = 0
       while idx > -1*(len(cost)+1):
        if cost[idx-1] > cost[idx-2]:
            minCost += cost[idx-2]
            idx = idx -2
        else:
            minCost += cost[idx-1]
            idx = idx -1

        
        return minCost
        
