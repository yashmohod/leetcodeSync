class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        tt={}
        for i in t:
            tt[i]= tt.get(i,0)+1
        ss={}
        for i in s:
            ss[i]= ss.get(i,0)+1
        for k in ss.keys():
            if k not in tt:
                return False
            else:
                if tt[k] !=ss[k]:
                    return False

        
        return True
        
