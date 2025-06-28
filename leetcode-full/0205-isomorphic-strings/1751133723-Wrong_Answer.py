class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ss = {}
        tt = {}

        for i in s:
            if i in ss:
                ss[i] += 1
            else:
                ss[i] = 1
        for i in t:
            if i in tt:
                tt[i] += 1
            else:
                tt[i] = 1
        
        ss = list(ss.values())
        tt = list(tt.values())
        for i in tt:
            try:
                ss.remove(i)
            except:
                return False
        if len(ss)>0:
            return False
        else:
            return True

            
