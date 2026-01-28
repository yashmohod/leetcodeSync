class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        m = len(potions)
        res = []

        for spell in spells:
            l, r = 0, m  # [l, r) search space
            while l < r:
                mid = (l + r) // 2
                if potions[mid] * spell >= success:
                    r = mid
                else:
                    l = mid + 1
            res.append(m - l)

        return res
