class Solution:
    def countSegments(self, s: str) -> int:
        if s == ""  :
            return 0 
        
        s = s.split(" ")
        if "" in s :
            s.remove("")
        if " " in s :
            s.remove(" ")
        return len(s)
