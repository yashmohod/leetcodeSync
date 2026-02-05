class Solution:
    def minOperations(self, s: str) -> int:
        l,r=0,0
        for i in range(len(s)):
            j = int(s[i])
            e = i%2
            o = (i+1)%2
            l+=1 if j^e else 0
            r+=1 if j^o else 0

        return min(l,r)
