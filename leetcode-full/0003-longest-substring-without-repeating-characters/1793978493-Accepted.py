class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        res = 0 
        l,r = 0,0
        v = set()
        n=len(s) 
        while l < n:

            if r < n and s[r] not in v :
                v.add(s[r])
                r+=1
            else:
                v.remove(s[l])
                l+=1     

            res = max(r-l,res)
        return res
