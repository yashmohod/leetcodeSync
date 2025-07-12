class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        l,r = 0,0 

        while r < len(t):
            if l < len(s) and  s[l] == t[r]:
                l+=1
            r+=1
        
        if l == len(s):
            return True
        else:
            return False
