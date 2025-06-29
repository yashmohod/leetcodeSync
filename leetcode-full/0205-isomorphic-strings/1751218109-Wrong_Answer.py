class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ll = {}

        for i in range(len(t)):

            if s[i] in ll :
                if ll[s[i]] != t[i]:
                    return False
            else:
                ll[s[i]] = t[i]

        
        return True 
