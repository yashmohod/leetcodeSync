class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ss = 0

        for i in t : 
            if ss< len(s) and s[ss] == i:
                ss +=1

        return ss == len(s)
