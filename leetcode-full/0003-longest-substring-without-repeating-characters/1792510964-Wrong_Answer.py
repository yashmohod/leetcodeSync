class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0 
        l,r=0,0
        cur = set()

        while l < len(s)-1:

            while s[r] in cur and l < r: 
                cur.remove(s[l])
                l+=1
            
            cur.add(s[r])
            r+=1 if r < len(s)-1 else 0
            res = max(r-l,res)
        
        return res
            





