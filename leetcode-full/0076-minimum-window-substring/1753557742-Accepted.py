class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        tset = {}
        for i in t:
            tset[i] = 1 + tset.get(i,0)
        tlen = len(tset)
        al,ar = 0,float('inf')
        l,r = 0,0
        slen = 0 
        sset = {}
        while r < len(s):
            
            if s[r] in tset:
                sset[s[r]] = 1 + sset.get(s[r],0)
                if sset.get(s[r],0) == tset.get(s[r],0):
                    slen += 1
            
            while slen == tlen:
                if  ar-al > r-l:
                    al,ar = l,r
                if s[l] in sset:
                    sset[s[l]] -= 1
                    if sset[s[l]] < tset[s[l]]:
                        slen -= 1                    
                
                l+=1
                
            r+=1

        
        return "" if ar == float('inf') else s[al:ar+1]
