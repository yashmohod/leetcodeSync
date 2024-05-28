class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        end = k
        vow = "aeiouAEIOU"
        la=-float('inf')
        while end <len(s):
            count=0
            for i in s[start:end]:
                if i in vow:
                    count+=1
            if count > la :
                la=count
            start+=1
            end+=1
        return la
