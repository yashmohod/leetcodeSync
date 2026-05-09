class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) ==1:
            return s
        res = -1
        resstr = ""
        for c in range(len(s)):
            
            d = 0
            while c-d >= 0 and c+d < len(s) and s[c-d] == s[c+d]:
                if res < d*2+1:
                    res = d*2 +1
                    resstr = s[c-d:c+d+1]
                d+=1
            
            l,r = 0,1
            while c-l >= 0 and c+r < len(s) and s[c-l] == s[c+r]:
                print(s[c-l:c+r+1],c-l,c+r+1,res)
                if res < r+l+1: 
                    res = r+l+1
                    resstr = s[c-l:c+r+1]
                l+=1
                r+=1
        return resstr
            

            
