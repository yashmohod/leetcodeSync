class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)> 0 and s[0] =="0":
            return 0
        res = -1
        valid = set([str(i) for i in range(26)])
        for i in range(len(s)):

            if s[i] != "0":
                res+=1
            if s[i-1:i+1] in valid:
                res+=1
        return res


