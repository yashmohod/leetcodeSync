class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        pairs=[]
        potions.sort()
        print(potions)
        for spell in spells:
            l=0
            r=len(potions)-1
            c=round((r+l)/2)
            found = False
            # print( potions[-1] * spell <success)
            if potions[-1] * spell <success:
                pairs.append(0)
            else:
                while spell*potions[c] >= success:
                    if r-l ==1:
                        if spell*potions[l]< success:
                            # print("here1")
                            pairs.append(len(potions) - c - 1)
                            found = True
                            break
                        elif spell*potions[r]< success:
                            pairs.append(len(potions) - c - 1)
                            # print("here2")
                            found = True
                            break
                        else:
                            pairs.append(0)
                            found = True
                            break
                    if spell*potions[c] >= success:
                        r=c
                    c=round((r+l)/2)
                if not found:
                    # print("here3")
                    pairs.append(len(potions) - c - 1)
                
        return pairs
