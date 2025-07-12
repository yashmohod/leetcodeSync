class Solution:
    def countSegments(self, s: str) -> int:
        if s == ""  :
            return 0 
        
        s = s.split(" ")
        while "" in s :

            s.remove("")
        while " " in s :
            s.remove(" ")
        return len(s)
