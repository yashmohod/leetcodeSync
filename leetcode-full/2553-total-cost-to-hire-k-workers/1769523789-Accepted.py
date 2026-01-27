class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        lh, rh = [], []
        i, j = 0, n - 1

        # preload left side
        for _ in range(candidates):
            if i <= j:
                heapq.heappush(lh, (costs[i], i))
                i += 1

        # preload right side
        for _ in range(candidates):
            if i <= j:
                heapq.heappush(rh, (costs[j], j))
                j -= 1

        total = 0
        for _ in range(k):
            if not rh or (lh and lh[0] <= rh[0]):  # compares (cost, index)
                c, idx = heapq.heappop(lh)
                total += c
                if i <= j:
                    heapq.heappush(lh, (costs[i], i))
                    i += 1
            else:
                c, idx = heapq.heappop(rh)
                total += c
                if i <= j:
                    heapq.heappush(rh, (costs[j], j))
                    j -= 1

        return total
