class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        cur = set()

        l = 0 
        r = 0 
        N = len(s)
        while r < N:

            if s[r] not in cur:
                cur.add(s[r])
                r+=1
            else:
                while s[r] in cur and l<r:
                    cur.remove(s[l])
                    l+=1
            
            res = max(res,r-l)
        return res

