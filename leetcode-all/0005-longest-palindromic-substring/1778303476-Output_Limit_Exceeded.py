class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) ==1:
            return s
        def isPal(ss):
            for i in range(len(ss)):
                if ss[i] != ss[len(ss)-1-i]:
                    return False
            return True

        res = 0
        strs = 0
        for l in range(len(s)):
            for r in range(l,len(s)+1):
                print(s[l:r])
                if isPal(s[l:r]) and  res < len(s[l:r]):
                    res = len(s[l:r])
                    strs =s[l:r]
        return strs
        
