class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        end = k
        vow = "aeiouAEIOU"
        sum=0
        for i in s[start:end]:
                if i in vow:
                    sum+=1
        la = sum
        while end <len(s):
            if s[start] in vow:
                sum-=1 
            if s[end] in vow:
                sum+=1
            la = max(la,sum)
            start+=1
            end+=1
        return la
