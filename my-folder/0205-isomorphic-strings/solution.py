class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ll = {}
        lll = {}

        for i in range(len(t)):

            if s[i] in ll :
                if ll[s[i]] != t[i]:
                    return False
            else:
                ll[s[i]] = t[i]
            
            if t[i] in lll :
                if lll[t[i]] != s[i]:
                    return False
            else:
                lll[t[i]] = s[i]

        
        return True 
