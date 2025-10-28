class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sc=0
        tc=0
        while sc < len(s):

            while s[sc] !=t[tc] and tc<len(t):
                tc+=1
            if tc >= len(t):
                return False
            sc+=1
            tc=sc

        return False
