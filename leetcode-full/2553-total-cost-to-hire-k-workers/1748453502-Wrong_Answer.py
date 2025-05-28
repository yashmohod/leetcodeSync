class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost = 0
        c = candidates
        for i in range(k) :
            cur = 0 
            if c*2 < len(costs):
                cur = min(min(costs[:c]),min(costs[-c:]))
            else:
                cur = min(costs)
            cost += cur
            costs.remove(cur)
            
        

        return cost

