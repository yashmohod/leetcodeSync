class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        t = list(t)
        # s = list(s)
        for i in t :
            print(i,not(i in s))
            if not(i in s) :
                return i 
