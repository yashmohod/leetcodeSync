class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        ss = []
        tt = []

        for i in s:
            if i == "#":
                if len(ss)>0:
                    ss.pop()
                else:
                    ss.append(i)

        for i in t:
            if i == "#":
                if len(tt)>0:
                    tt.pop()
                else:
                    tt.append(i)
        
        return tt == ss

                
