class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0 
        l,r=0,0
        cur = set()

        while l < len(s):
            if r < len(s) and s[r] not in cur:
                cur.add(s[r])
                r+=1
                res = max(r-l,res)
            else:
                cur.remove(s[l])
                l+=1
            
        return res
            





