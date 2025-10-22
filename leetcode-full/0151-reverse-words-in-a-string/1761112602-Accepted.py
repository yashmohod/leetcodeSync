class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split(" ")

        # while  " " in s:
        #     s.remove(" ")
        
        while  "" in s:
            s.remove("")
        
        res = ""

        for i in range(len(s)-1,-1,-1):
            res+=s[i]+" "
        
        return res[:-1]
