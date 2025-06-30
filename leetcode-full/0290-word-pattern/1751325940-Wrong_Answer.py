class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        p = list(pattern)
        s = s.split(" ")
        po = {}
        op = {}

        for i in range(len(p)):
            if p[i] in po:
                if po[p[i]] != s[i]:
                    return False
            else:
                po[p[i]] = s[i]
            
            if s[i] in op:
                if op[s[i]] != p[i]:
                    return False
            else:
                op[s[i]] = p[i]
        
        return True
