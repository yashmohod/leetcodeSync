class Solution:
    def countSegments(self, s: str) -> int:
        if s == ""  :
            return 0 
        
        s = s.split(" ")
        s.remove("")
        s.remove(" ")
        return len(s)
