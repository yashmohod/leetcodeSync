class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        l,r = 0,0 

        last = 0

        while r < len(s):

            if r+1 in range(len(s)+1):
                if  s[r] in s[l:r]:
                    l +=1
                else:
                    if last < len(s[l:r+1]):
                        last = len(s[l:r+1] )
                    r+=1

            

        return last

        

