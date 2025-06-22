class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 1:
            return 1

        l,r = 0,0 

        last = ""

        while r < len(s):

            if r+1 in range(len(s)):
                if  s[r] in s[l:r]:
                    l = r 
                else:
                    if len(last) < len(s[l:r+1]):
                        last = s[l:r+1]  
            r+=1

            

        return len(last)

        

