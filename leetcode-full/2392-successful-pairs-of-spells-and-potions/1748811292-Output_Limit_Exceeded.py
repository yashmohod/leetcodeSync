class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        pairs=[]
        potions.sort()
        # print(potions)
        for spell in spells:
           
           if spell * potions[-1] <  success:
            pairs.append(0)

           else:
            l = 0 
            r = n - 1 
            c = round((l+r)/2)

            while True:

                print(c)
                if c == 0 and spell * potions[c] < success:
                    if spell * potions[c+1] < success:
                        pairs.append(0)
                    else:
                        pairs.append(n-(c+1))
                    break
                elif c == 0 and spell * potions[c] >= success:
                    pairs.append(n-(c))
                    break
                if c == n-1 and spell * potions[c] < success:
                    pairs.append(0)
                elif c == n-1 and spell * potions[c] >= success:
                    pairs.append(1)
                    break

                lr = spell * potions[c-1] >= success
                cr = spell * potions[c] >= success
                rr = spell * potions[c+1] >= success

                if lr == False and cr == False and rr == False:
                    l = c+1
                if lr == True and cr == True and rr == True:
                    r = c

                
                if lr == False and cr == False and rr == True:
                    pairs.append(n-(c+1))
                    break
                if lr == False and cr == True and rr == True:
                    pairs.append(n-(c))
                    break

                
                c = round((l+r)/2)

        return pairs

                
