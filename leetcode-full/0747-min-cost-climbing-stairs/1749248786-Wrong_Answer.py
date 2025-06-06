class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = 0 
        idx = 0
        while idx > -1*(len(cost)-1):   
            # print(idx,-1*(len(cost)+1))
            if cost[idx-1] > cost[idx-2] or cost[idx-1] == cost[idx-2]:
                print(cost[idx-2])
                minCost += cost[idx-2]
                idx -= 2
            else:
                print(cost[idx-1])
                minCost += cost[idx-1]
                idx -= 1

        
        return minCost
        
