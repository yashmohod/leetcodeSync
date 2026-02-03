class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        p = set()
        l,r =0,0
        lg = 0
        while r <len(s):
            if s[r] in p:
                while s[r] in p and l<r:
                    p.remove(s[l])
                    l+=1

            p.add(s[r])
            r+=1 
            lg = max(lg,r-l)
        return lg 
