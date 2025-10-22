class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        vo = list("aeiouAEIOU")

        l,r = 0,len(s)-1

        while l<r:
            while s[l] not in vo or not s[l].isalnum():
                l+=1
            while s[r] not in vo or not s[r].isalnum():
                r-=1
            if l > r:
                break
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
        
        return "".join(s)
