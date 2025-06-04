class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur = 0 
        costSum = 0 

        if cost[0] > cost[1]:
            cur = 1
        else: 
            cur = 0
        costSum += cost[cur]

        while cur < len(cost)-2:
            if cost[cur+2] > cost[cur+1]:
                cur +=1
            else:
                cur +=2
            costSum += cost[cur]
        
        return costSum 
                
                
