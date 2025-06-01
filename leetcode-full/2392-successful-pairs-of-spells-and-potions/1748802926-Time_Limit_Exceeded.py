class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        pairs=[]
        potions.sort()

        for spell in spells:
            found=False
            for potion in potions:
                if potion * spell >= success:
                    cur = potions.index(potion)
                    pairs.append(len(potions)-cur)
                    found=True
                    break
            if not found:
                pairs.append(0)
        return pairs
