class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        l,r=0,0
        seen = set()
        while l < len(s):
            if r > len(s):
                l+=1
                r=l 
                continue
            if r < len(s) and r-l > 1 and s[r] == s[l]:
                c=l+1
                while c < r:
                    ss =s[l]+s[c]+s[r]
                    if ss not in seen:
                        seen.add(ss)
                    c+=1
            r+=1
        
        return len(seen)
             
        

