class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split(" ")

        # while  " " in s:
        #     s.remove(" ")
        
        while  "" in s:
            s.remove("")
        
        l,r = 0,len(s)-1
        

        res = ""

        for i in range(len(s)-1,-1,-1):
            res+=s[i]+" "
        
        return res[:-1]
