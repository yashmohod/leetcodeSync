class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ss = {}
        tt = {}

        for i in s :
            ss[i] = ss.get(i,0)+1 
        for i in t :
            tt[i] = tt.get(i,0)+1

        for key,val in ss.items():
            if key not in tt or tt[key] != val:
                return False

        return True
