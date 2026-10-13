class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        t = set()
        res = 0
        l,r = 0,0
        N = len(s)
        while r < N:
            while s[r] in t:
                t.remove(s[l])
                l+=1
            t.add(s[r])
            res = max(res,len(t))
            r+=1
        
        return res
